from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_kb = ReplyKeyboardMarkup(resize_keyboard=True)

help_btn = KeyboardButton('Помощь')
desc_btn = KeyboardButton('F.A.Q')
events_btn = KeyboardButton('Посмотреть мероприятия')

start_kb.add(help_btn).insert(desc_btn)
start_kb.insert(events_btn)

#--------------------------------------#

events_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu_btn = KeyboardButton('Главное меню')
kizaru_btn = KeyboardButton('kizaru')
bbt_btn = KeyboardButton('Big Baby Tape')

events_kb.add(kizaru_btn, bbt_btn).insert(main_menu_btn)

#-----------------KIZARU---------------------#

kizaru_buy_ticket_kb = InlineKeyboardMarkup(row_width=1)
kizaru_buy_ticket_btn = InlineKeyboardButton(url='https://google.com', text='Приобрести билет')

kizaru_buy_ticket_kb.add(kizaru_buy_ticket_btn)

#-----------------Big Baby Tape---------------------#

babytape_buy_ticket_kb = InlineKeyboardMarkup(row_width=1)
babytape_buy_ticket_btn = InlineKeyboardButton(url='https://google.com', text='Приобрести билет')

babytape_buy_ticket_kb.add(babytape_buy_ticket_btn)