from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from states import data
from keyboard import markup_start, markup_place
import utils.db_api.quick_commands_request as commands
import traceback
#Handler for /start
@dp.message_handler(text = '/start')
async def command_start(message = types.Message):
    await message.answer(f"Приветствуем тебя!\n"+
                         "Здесь ты можешь:\n"+
                         "-узнать информацию о нашем клубе✉\n"+
                         "-забронировать железо📆", reply_markup=markup_start )
#Start to process reserve
@dp.callback_query_handler(text = 'reserve')
async def reserve(call: types.CallbackQuery):
    try:
        await commands.select_request(call.message.from_user.id)
        await call.message.edit_text("Ты уже подал заявку. Дождись рассмотрения")
    except Exception as exc:

        await call.message.edit_text("Выбери зал: ")
        await call.message.edit_reply_markup(reply_markup=markup_place)
        await data.place.set() #place.py