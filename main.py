from aiogram import executor, Bot, types, Dispatcher
from dispatcher import dp
import handlers


if __name__ == '__main__':
    executor.start_polling(dp)