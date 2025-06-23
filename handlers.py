from aiogram import Dispatcher, types, Bot, executor
import texts_ru, texts_en
from texts_ru import GREETINGS
from dispatcher import dp

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.reply(GREETINGS)