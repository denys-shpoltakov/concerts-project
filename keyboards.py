from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(resize_keyboard=True)
help_btn = KeyboardButton('Помощь')
desc_btn = KeyboardButton('Описание бота')

start_kb.add(help_btn).insert(desc_btn)

#--------------------------------------#

events_kb = ReplyKeyboardMarkup(resize_keyboard=True)
kizaru_btn = KeyboardButton('kizaru')

events_kb.add(kizaru_btn)