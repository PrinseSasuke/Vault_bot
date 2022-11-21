from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db_api.db_gino import db
BOT_TOKEN = "5639036445:AAFtX7V6v3yiu-sJzMia_CKq6ZsGElxkfqg"

bot = Bot(token = BOT_TOKEN, parse_mode= types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage =storage)
__all__ = ['bot', 'storage', 'dp', 'db']
