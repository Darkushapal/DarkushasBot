from aiogram import types, F, Router, types
from aiogram.filters import Command
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.filters import CommandObject
from aiogram import html

router = Router()

mylist = [1, 2, 3]


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


@router.message(Command("test1"))
async def cmd_test1(message: types.Message):
    await message.reply("Test1")


@router.message(Command("Roll1"))
async def cmd_dice1(message: types.Message):
    await message.answer_dice(emoji="🎲")


@router.message(Command("add_to_list"))
async def cmd_add_to_list(message: types.Message, mylist: list[int]):
    mylist.append(7)
    await message.reply("Добавлено число семь!")


@router.message(Command("show_list"))
async def cmd_show_list(message: types.Message, mylist: list[int]):
    await message.answer(f"Ваш список: {mylist}")


@router.message(Command("name"))
async def cmd_name(message: types.Message, command: CommandObject):
    if command.args:
        await message.answer(f"Привет, {html.bold(html.quote(command.args))}")

    else:
        await message.answer("Пожалуйста, укажи своё имя после команды /name!")
