import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

BOT_TOKEN = 5650181298:AAEojGlUYsOqPY4wBDUTvtYxGFqZOGU2P0A

TOKEN = getenv("BOT_TOKEN")