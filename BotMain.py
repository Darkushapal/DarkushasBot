import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from config import config
from handlers import router

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")

dp = Dispatcher()

dp.include_router(router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
