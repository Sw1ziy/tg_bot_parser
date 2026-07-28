from aiogram import Router, types
from aiogram.filters import Command

from config import SOURCE_CHANNEL

router = Router(name="info")

@router.message(Command("info"))
async def info_handler(message: types.Message):
    await message.answer(
        "Это бот-парсер Telegram-канала.\n"
        f"Источник, который отслеживается: @{SOURCE_CHANNEL}\n"
        "Новые посты автоматически пересылаются сюда."
    )
