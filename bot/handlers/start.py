from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import SOURCE_CHANNEL

router = Router(name="start")


@router.message(CommandStart())
async def start_handler(message: types.Message):
    text = (
        f"👋 <b>Привет, {message.from_user.first_name}!</b>\n"
        f"<i>Бот запущен и готов к работе</i>\n\n"
        f"➖➖➖➖➖➖➖➖\n"
        f"🆔 Твой chat_id\n"
        f"<code>{message.chat.id}</code>\n"
        f"➖➖➖➖➖➖➖➖\n\n"
        f"Выбери, что нужно 👇"
    )

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="ℹ️ О боте", callback_data="show_info"),
                InlineKeyboardButton(text="💰 Баланс", callback_data="show_balance"),
            ],
            [
                InlineKeyboardButton(text="📡 Открыть канал", url=f"https://t.me/{SOURCE_CHANNEL}"),
            ],
        ]
    )

    await message.answer(text, reply_markup=keyboard, parse_mode="HTML")


@router.callback_query(lambda c: c.data == "show_info")
async def info_callback(callback: types.CallbackQuery):
    from config import SOURCE_CHANNEL
    text = (
        "ℹ️ <b>Как работает этот бот</b>\n\n"
        f"📡 Источник: <code>@{SOURCE_CHANNEL}</code>\n\n"
        "Бот в реальном времени следит за каналом и как только там "
        "выходит новый пост — сразу пересылает его сюда.\n\n"
        "➖➖➖➖➖➖➖➖\n"
        "🔁 <b>Что переносится:</b>\n"
        "📝 текст поста\n"
        "🖼 фото и видео\n"
        "📎 документы\n"
        "🔘 кнопки-ссылки (если есть)\n"
        "➖➖➖➖➖➖➖➖\n\n"
        "Не нужно самому сидеть в канале — всё важное придёт сюда автоматически ⚡️"
    )
    await callback.message.answer(text, parse_mode="HTML")
    await callback.answer()


@router.callback_query(lambda c: c.data == "show_balance")
async def balance_callback(callback: types.CallbackQuery):
    text = (
        "💰 <b>Общий баланс:</b> 0 $\n\n"
        "💰 <b>Баланс биржи BIBYT:</b> 0 $\n"
        "💰 <b>Баланс биржи BITGET:</b> 0 $\n"
        "💰 <b>Баланс биржи Binance:</b> 0 $\n"
        "💰 <b>Баланс биржи OURBIT:</b> 0 $\n"
        "💰 <b>Баланс биржи MEXC:</b> 0 $\n"
        "💰 <b>Баланс биржи GATE:</b> 0 $"
    )
    await callback.message.answer(text, parse_mode="HTML")
    await callback.answer()