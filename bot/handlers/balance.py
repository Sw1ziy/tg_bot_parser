from aiogram import Router, types
from aiogram.filters import Command

router = Router(name="balance")


@router.message(Command("balance"))
async def balance_handler(message: types.Message):
    # Пока заглушка. Сюда позже подключим реальную логику
    # (например, чтение баланса из базы данных).
    fake_balance = 0
    await message.answer(f"Ваш баланс: {fake_balance} у.е.")
