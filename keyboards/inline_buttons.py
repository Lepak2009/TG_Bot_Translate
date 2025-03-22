from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

lang_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Англійська", callback_data="lang_en"),
         InlineKeyboardButton(text="Українська", callback_data="lang_uk")]
    ]
)

save_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Зберегти вибір", callback_data="save_langs")],
        [InlineKeyboardButton(text="Вибрати інші мови", callback_data="change_langs")]
    ]
)
