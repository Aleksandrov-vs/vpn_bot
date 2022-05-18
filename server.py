import logging
import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, executor, types
from app.keyboards import auth_kbd
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from app.hendlers.users import auth

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())
auth.register_handlers_auth(dp)





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
