import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH")
SOURCE_CHANNEL = os.getenv("SOURCE_CHANNEL")
TARGET_CHAT_ID = int(os.getenv("TARGET_CHAT_ID", "0"))

# Небольшая проверка, чтобы сразу было видно, если что-то забыли заполнить
_required = {
    "BOT_TOKEN": BOT_TOKEN,
    "API_ID": API_ID,
    "API_HASH": API_HASH,
    "SOURCE_CHANNEL": SOURCE_CHANNEL,
    "TARGET_CHAT_ID": TARGET_CHAT_ID,
}

def check_config():
    missing = [name for name, value in _required.items() if not value]
    if missing:
        raise RuntimeError(
            f"В .env не заполнены обязательные поля: {', '.join(missing)}"
        )
