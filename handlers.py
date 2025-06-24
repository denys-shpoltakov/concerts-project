from aiogram import Dispatcher, types, Bot, executor
import texts_ru, texts_en
from texts_ru import GREETINGS, HELP_CMD
from dispatcher import dp

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.reply(GREETINGS)

@dp.message_handler(commands=['help'])
async def start_cmd(message: types.Message):
    await message.reply(HELP_CMD)