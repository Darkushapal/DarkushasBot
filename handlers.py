from aiogram import types, F, Router, types
from aiogram.filters import Command
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.filters import CommandObject
from aiogram import html
from datetime import datetime
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder
import random

router = Router()

mylist = [1, 2, 3]


@router.message(Command("start"))
async def cmd_start_buttons(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="Geolocation"),
        types.KeyboardButton(text="Contact INFO")
    )
    builder.row(types.KeyboardButton(
        text="Создать викторину",
        request_poll=types.KeyboardButtonPollType(type="quiz"))
    )
    builder.row(
        types.KeyboardButton(
            text="Выбрать премиум пользователя",
            request_user=types.KeyboardButtonRequestUser(
                request_id=1,
                user_is_premium=True
            )
        ),
        types.KeyboardButton(
            text="Выбрать супергруппу с форумами",
            request_chat=types.KeyboardButtonRequestChat(
                request_id=2,
                chat_is_channel=False,
                chat_is_forum=True
            )
        )
    )

    await message.answer(
        "Выберите действие:",
        reply_markup=builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
    )


@router.message(F.user_shared)
async def on_user_shared(message: types.Message):
    print(
        f"Request {message.user_shared.request_id}. "
        f"User ID: {message.user_shared.user_id}"
    )


@router.message(F.chat_shared)
async def on_user_shared(message: types.Message):
    print(
        f"Request {message.chat_shared.request_id}. "
        f"User ID: {message.chat_shared.chat_id}"
    )


@router.message(Command("inline_url"))
async def cmd_inline_url(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="GitHub", url="https://github.com")
    )

    #user_id = 1234567890
    #chat_info = await message.bot.get_chat(user_id)
    #if not chat_info.has_private_forwards:
    #    builder.row(types.InlineKeyboardButton(
    #        text="Какой-то пользователь",
    #        url=f"tg://user?id={user_id}")
    #    )

    await message.answer(
        'Chose a link',
        reply_markup=builder.as_markup()
    )


@router.message(Command("random"))
async def cmd_random(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    await message.answer(
        "Нажмите на кнопку, чтобы бот отправил число от 1 до 10",
        reply_markup=builder.as_markup()
    )


@router.callback_query(F.data == "random_value")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(str(random.randint(1, 10)))
    await callback.answer()


@router.message(Command("name"))
async def cmd_name(message: types.Message, command: CommandObject):
    if command.args:
        await message.answer(f"Привет, {html.bold(html.quote(command.args))}")

    else:
        await message.answer("Пожалуйста, укажи своё имя после команды /name!")

# @router.message(F.text)
# async def echo_with_time(message: types.Message):
#    time_now = datetime.now().strftime("%H:%M")
#    added_text = html.underline(f"Создано в {time_now}")
#    await message.answer(f"{message.html_text}\n\n{added_text}", parse_mode="HTML")

# @router.message(F.text)
# async def echo_with_time(message: types.Message):
#    data = {
#        "url": "<N/A>",
#        "email": "<N/A>",
#        "code": "<N/A>"
#    }
#    entities = message.entities or []
#    for item in entities:
#        if item.type in data.keys():
#            data[item.type] = item.extract_from(message.text)
#
#    await message.reply(
#        "Вот что я нашёл:\n"
#        f"URL: {html.quote(data['url'])}\n"
#        f"E-mail: {html.quote(data['email'])}\n"
#        f"Пароль: {html.quote(data['code'])}"
#    )
