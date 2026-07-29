import asyncio
import os

from aiogram import Bot
from telethon import events

from config import BOT_TOKEN, SOURCE_CHANNEL, TARGET_CHAT_ID, check_config
from parser.client import telethon_client

bot = Bot(token=BOT_TOKEN)

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


@telethon_client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    message = event.message
    text = message.raw_text or ""

    try:
        if message.media:
            file_path = await message.download_media(file=DOWNLOAD_DIR + "/")
            if not file_path:
                if text:
                    await bot.send_message(TARGET_CHAT_ID, text)
                return
            lower = file_path.lower()
            with open(file_path, "rb") as f:
                if lower.endswith((".jpg", ".jpeg", ".png", ".webp")):
                    await bot.send_photo(TARGET_CHAT_ID, photo=f, caption=text[:1024] or None)
                elif lower.endswith((".mp4", ".mov")):
                    await bot.send_video(TARGET_CHAT_ID, video=f, caption=text[:1024] or None)
                else:
                    await bot.send_document(TARGET_CHAT_ID, document=f, caption=text[:1024] or None)

            os.remove(file_path)

        elif text:
            await bot.send_message(TARGET_CHAT_ID, text)

    except Exception as e:
        print(f"Error processing message: {e}")


async def main():
    check_config()
    await telethon_client.start()
    print(f"Parsing start, chek chanel: {SOURCE_CHANNEL}")
    await telethon_client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
