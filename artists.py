from aiogram import Dispatcher, types, Bot, executor
from aiogram.dispatcher.filters import Text
from keyboards import start_kb, events_kb
from dispatcher import dp
from aiogram.types import InputFile
from texts_ru import KIZARU_TEXT


@dp.message_handler(Text(equals='kizaru'))
async def kizaru_cmd(message: types.Message):
    kizaru_video = InputFile('videos/kizaru.mp4')
    await message.bot.send_video(chat_id=message.from_user.id,
                                 caption=KIZARU_TEXT,
                                 video=kizaru_video,
                                 reply_markup=events_kb)