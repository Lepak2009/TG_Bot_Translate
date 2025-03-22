from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.inline_buttons import lang_buttons, save_buttons

router = Router()
user_data = {}

@router.callback_query(F.data.in_(["lang_en", "lang_uk"]))
async def select_source_lang(callback: CallbackQuery):
    user_id = callback.from_user.id

    # Перевіряємо, чи користувач уже вибрав вихідну мову
    if user_id not in user_data:
        user_data[user_id] = {"source_lang": callback.data.split("_")[1]}
        await callback.message.answer("Чудово! Виберіть мову перекладу:", reply_markup=lang_buttons)
    else:
        user_data[user_id]["target_lang"] = callback.data.split("_")[1]
        await callback.message.answer("Вибір збережено! Тепер введіть текст для перекладу.")
