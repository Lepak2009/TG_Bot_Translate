from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Go translate")],
        [KeyboardButton(text="Додаткова інформація")],
        [KeyboardButton(text="Завершити переклад")]
    ],
    resize_keyboard=True
)
