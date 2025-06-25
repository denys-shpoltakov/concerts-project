from aiogram import executor, Bot, types, Dispatcher
from dispatcher import dp
import handlers
import artists


if __name__ == '__main__':
    executor.start_polling(dp)