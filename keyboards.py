from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(resize_keyboard=True)
help_btn = KeyboardButton('/help')

start_kb.add(help_btn)