from aiogram import Dispatcher, types, Bot, executor
import texts_ru, texts_en
from texts_ru import GREETINGS, HELP_CMD, DESC_CMD
from dispatcher import dp
from keyboards import start_kb

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.reply(GREETINGS,
                        reply_markup=start_kb)

@dp.message_handler(commands=['help'])
async def help_cmd(message: types.Message):
    await message.reply(HELP_CMD)

@dp.message_handler(commands=['description'])
async def desc_cmd(message: types.Message):
    await message.bot.send_message(chat_id=message.from_user.id,
                                   text=DESC_CMD)