
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from handlers import inline_handlers, reply_handlers
from config import TOKEN
from handlers import translate_handler

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(reply_handlers.router)
    dp.include_router(inline_handlers.router)
    dp.include_router(translate_handler.router)

    await bot.set_my_commands([
        BotCommand(command="start", description="Запустити бота"),
    ])

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
