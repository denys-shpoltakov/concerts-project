from aiogram import Dispatcher, types, Bot, executor
from aiogram.dispatcher.filters import Text
from keyboards import start_kb, events_kb, kizaru_buy_ticket_kb, babytape_buy_ticket_kb, boris_brejcha_buy_ticket_kb
from dispatcher import dp
from aiogram.types import InputFile
from texts_ru import KIZARU_TEXT, BBT_TEXT


@dp.message_handler(Text(equals='kizaru'))
async def kizaru_cmd(message: types.Message):
    kizaru_photo = InputFile('photos/kizaru_conc.jpg')
    await message.bot.send_photo(chat_id=message.from_user.id,
                                 caption=KIZARU_TEXT,
                                 photo=kizaru_photo,
                                 reply_markup=kizaru_buy_ticket_kb)
    
@dp.message_handler(Text(equals='Big Baby Tape'))
async def kizaru_cmd(message: types.Message):
    bbt_photo = InputFile('photos/bigbabytape.jpg')
    await message.bot.send_photo(chat_id=message.from_user.id,
                                 caption=BBT_TEXT,
                                 photo=bbt_photo,
                                 reply_markup=babytape_buy_ticket_kb)

@dp.message_handler(Text(equals='Boris Brejcha'))
async def kizaru_cmd(message: types.Message):
    boris_brejcha_photo = InputFile('photos/boris-brejcha.jpg')
    await message.bot.send_photo(chat_id=message.from_user.id,
                                 caption=BBT_TEXT,
                                 photo=boris_brejcha_photo,
                                 reply_markup=boris_brejcha_buy_ticket_kb)