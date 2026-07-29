import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN, check_config
from bot.handlers import start, balance, info
from parser.channel_parser import main as run_parser

logging.basicConfig(level=logging.INFO)


async def run_bot():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(balance.router)
    dp.include_router(info.router)

    print("Bot starting...")
    await dp.start_polling(bot)

async def main():
    check_config()
    await asyncio.gather(
        run_bot(),
        run_parser(),
    )


if __name__ == "__main__":
    asyncio.run(main())