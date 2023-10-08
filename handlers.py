from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def cmd_start(msg: Message):
    await msg.answer("Hello!")


@router.message(Command("test1"))
async def cmd_test1(msg: Message):
    await msg.reply("Test1")

@router.message(Command("Roll"))
async def cmd_dice(msg: Message):
    await msg.answer_dice(emoji="🎲")
