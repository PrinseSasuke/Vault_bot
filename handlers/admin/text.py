from aiogram import types
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from states import admin_data
from keyboard import markup_start, markup_place
from handlers.call_back_data import cb
import utils.db_api.quick_commands_request as commands
admin_id = '5785028847'

