from aiogram import Router, F
from aiogram.types import Message
from keyboards.reply_keyboards import reply_keyboard
from keyboards.inline_buttons import lang_buttons

router = Router()

@router.message(F.text == "/start")
async def start_command(message: Message):
    await message.answer("Привіт! Я бот для перекладу. Виберіть дію:", reply_markup=reply_keyboard)

@router.message(F.text == "Go translate")
async def go_translate(message: Message):
    await message.answer("Почнемо переклад! Виберіть основну мову:", reply_markup=lang_buttons)

@router.message(F.text == "Додаткова інформація")
async def additional_info(message: Message):
    await message.answer("Я допомагаю перекладати текст між мовами. Просто виберіть мови і введіть текст!")

@router.message(F.text == "Завершити переклад")
async def end_translation(message: Message):
    await message.answer("Ви завершили переклад. Якщо хочете продовжити, натисніть 'Go translate'.")
