from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from exchanges.registry import EXCHANGES

router = Router(name="balance")


def build_exchanges_keyboard() -> InlineKeyboardMarkup:
    buttons = []
    row = []
    for key, exchange in EXCHANGES.items():
        row.append(
            InlineKeyboardButton(text=exchange["title"], callback_data=f"balance:{key}")
        )
        if len(row) == 2:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)

    return InlineKeyboardMarkup(inline_keyboard=buttons)


@router.message(Command("balance"))
async def balance_handler(message: types.Message):
    await message.answer(
        "💰 <b>Выбери биржу</b>",
        reply_markup=build_exchanges_keyboard(),
        parse_mode="HTML",
    )


@router.callback_query(lambda c: c.data.startswith("balance:"))
async def exchange_balance_callback(callback: types.CallbackQuery):
    exchange_key = callback.data.split(":", 1)[1]
    exchange = EXCHANGES.get(exchange_key)

    if not exchange:
        await callback.answer("Биржа не найдена", show_alert=True)
        return

    balance = await exchange["get_balance"]()
    lines = "\n".join(f"🔹 {currency}: <code>{amount}</code>" for currency, amount in balance.items())

    text = (
        f"💰 <b>Баланс на {exchange['title']}</b>\n\n"
        f"{lines}"
    )

    await callback.message.answer(text, parse_mode="HTML")
    await callback.answer()