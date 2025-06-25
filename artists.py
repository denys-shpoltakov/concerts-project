from aiogram import Dispatcher, types, Bot, executor
from aiogram.dispatcher.filters import Text
from keyboards import start_kb, events_kb
from dispatcher import dp
from aiogram.types import InputFile
from texts_ru import KIZARU_TEXT


@dp.message_handler(Text(equals='kizaru'))
async def kizaru_cmd(message: types.Message):
    kizaru_photo = InputFile('photos/kizaru.jpg')
    await message.bot.send_photo(chat_id=message.from_user.id,
                                 caption=KIZARU_TEXT,
                                 photo=kizaru_photo,
                                 reply_markup=events_kb)