# Telegram-парсер канала + бот

## Структура

```
project/
├── .env                    # ваши реальные токены (не публикуйте!)
├── .env.example            # шаблон
├── config.py                # загрузка настроек
├── requirements.txt
├── bot/                     # логика бота (команды)
│   ├── main.py               # запуск бота
│   └── handlers/
│       ├── start.py          # /start
│       ├── balance.py        # /balance
│       └── info.py           # /info
└── parser/                  # логика парсинга канала
    ├── client.py              # настройка Telethon
    └── channel_parser.py      # слушает канал, шлёт в бота
```

## Установка

```bash
pip install -r requirements.txt --break-system-packages
```

Заполните `.env` своими данными (см. `.env.example`).

## Запуск

Бот и парсер - это два независимых процесса. Запускать нужно оба
(в двух разных терминалах/окнах):

```bash
# Терминал 1: бот с командами
python -m bot.main

# Терминал 2: парсер канала
python -m parser.channel_parser
```

При первом запуске парсера Telethon попросит номер телефона
и код подтверждения (вход под вашим личным аккаунтом, разово).

## Как добавить новую команду боту

1. Создайте файл `bot/handlers/my_command.py`:

```python
from aiogram import Router, types
from aiogram.filters import Command

router = Router(name="my_command")

@router.message(Command("mycommand"))
async def my_command_handler(message: types.Message):
    await message.answer("Ответ на новую команду")
```

2. Подключите его в `bot/main.py`:

```python
from bot.handlers import start, balance, info, my_command
...
dp.include_router(my_command.router)
```
