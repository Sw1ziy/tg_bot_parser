from aiogram import Router, types
from aiogram.filters import CommandStart

router = Router(name="start")

@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}!\n"
        f"Твой chat_id: {message.chat.id}\n\n"
        f"Доступные команды:\n"
        f"/start — приветствие\n"
        f"/info — информация о боте\n"
        f"/balance — баланс (заглушка)"
    )
