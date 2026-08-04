from aiogram import Router, types
from aiogram.filters import Command

router = Router(name="balance")


@router.message(Command("balance"))
async def balance_handler(message: types.Message):
    # Пока заглушка. Сюда позже подключим реальную логику
    # (например, чтение баланса из базы данных).
    fake_balance = 0
    BIBYT = 0
    BITGET = 0
    OURBIT = 0
    MEXC = 0
    GATE = 0

    await message.answer(f"Ваш баланс: {fake_balance, BIBYT, BITGET, OURBIT, MEXC,GATE } у.е.")
    await message.answer(f"Ваш баланс BIBYT: {fake_balance, BIBYT, BITGET, OURBIT, MEXC, GATE} у.е.")
    await message.answer(f"Ваш баланс BITGET: {fake_balance, BIBYT, BITGET, OURBIT, MEXC, GATE} у.е.")
    await message.answer(f"Ваш баланс OURBIT: {fake_balance, BIBYT, BITGET, OURBIT, MEXC, GATE} у.е.")
    await message.answer(f"Ваш баланс MEXC: {fake_balance, BIBYT, BITGET, OURBIT, MEXC, GATE} у.е.")
    await message.answer(f"Ваш баланс GATE: {fake_balance, BIBYT, BITGET, OURBIT, MEXC, GATE} у.е.")
