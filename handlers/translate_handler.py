from aiogram import Router
from aiogram.types import Message
from googletrans import Translator
from keyboards.inline_buttons import save_buttons
from handlers.inline_handlers import user_data  # Додаємо імпорт user_data
from aiogram import Router
from aiogram.types import Message
from deep_translator import GoogleTranslator
from keyboards.inline_buttons import save_buttons

router = Router()
translator = GoogleTranslator(source="auto", target="uk")  # або target="en"

@router.message()
async def translate_text(message: Message):
    translated_text = translator.translate(message.text)
    await message.answer(f"Переклад:\n{translated_text}", reply_markup=save_buttons)

router = Router()
translator = Translator()


@router.message()
async def translate_text(message: Message):
    user_id = message.from_user.id

    # Перевіряємо, чи користувач вибрав мови
    if user_id not in user_data or "source_lang" not in user_data[user_id] or "target_lang" not in user_data[user_id]:
        await message.answer("Будь ласка, спочатку виберіть мови.")
        return

    source_lang = user_data[user_id]["source_lang"]
    target_lang = user_data[user_id]["target_lang"]

    # Переклад тексту
    try:
        translated_text = translator.translate(message.text, src=source_lang, dest=target_lang).text
        await message.answer(f"Переклад:\n{translated_text}", reply_markup=save_buttons)
    except Exception as e:
        await message.answer("❌ Помилка перекладу. Спробуйте ще раз.")
        print(f"Translation error: {e}")
