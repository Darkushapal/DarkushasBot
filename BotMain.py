import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

import config
from handlers import router

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.BOT_TOKEN)

dp = Dispatcher()

dp.include_router(router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
