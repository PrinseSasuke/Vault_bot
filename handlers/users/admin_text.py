import sqlite3
from aiogram import  types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import bot, dp
import utils.db_api.quick_commands_request as commands
from handlers.call_back_data import cb
from keyboard import markup_mes_admin
from states import admin_data, data
@dp.message_handler(state = admin_data.text)
async def mess(message: types.Message, state:FSMContext):
    print('dsfsdfds')
    data = await state.get_data()
    answer = data['answer']
    user_id = data['user_id']
    request = await commands.select_request(user_id)
    text = message.text
    await bot.edit_message_text(chat_id=admin_id, message_id=message.message_id, text="Вы приняли заявку")
    await bot.send_message(user_id, text=f"ДАТА: {request.date}\n" +
                                         f"ЗАЛ: {request.place}\n" +
                                         f"ВРЕМЯ: {request.time}\n" + "Заявка принята")