from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from states import data

from keyboard import markup_count
from loader import bot
import utils.db_api.quick_commands_request as commands
from aiogram.utils.callback_data import CallbackData
#cb = CallbackData("fabnum", "action")
from handlers.call_back_data import cb
send_menu = InlineKeyboardMarkup(row_width=2)
send_menu.add(InlineKeyboardButton(text="Отправить", callback_data=cb.new(action="send")),
                InlineKeyboardButton(text="Заполнить заново", callback_data="resend"),
                InlineKeyboardButton(text="Добавить сообщение", callback_data="mail"))
@dp.callback_query_handler(text = ['0:00','1:00','2:00','3:00','4:00','5:00',
                                   '6:00','7:00','8:00','9:00','10:00','11:00',
                                   '12:00','13:00','14:00','15:00','16:00','17:00',
                                   '18:00','19:00','20:00','21:00','22:00','23:00'], state = data.time)
async def place(call: types.CallbackQuery, state:FSMContext):
   await state.update_data(time = call.data)
   await call.message.edit_text("Выбери кол-во мест: ")
   await call.message.edit_reply_markup(reply_markup=markup_count)
   await data.count.set()
   """"
    data = await state.get_data()
    place = data.get('place')
    date = data.get('date')
    time = data.get('time')
    place_text = ''
    if place == 'main':
        place_text = 'ОСНОВНОЙ'
    elif place == 'vip':
        place_text = 'VIP👑'
    elif place == 'ultra_vip':
        place_text = 'ULTRA_VIP👑'
    elif place == 'ps4':
        place_text = 'PS4🎮'
    await call.message.edit_text('Твоя заявка: \n'+
                                 'ЗАЛ: ' + place_text + '\n'+
                                 'ДАТА: '+ date + '\n'+
                                 'ВРЕМЯ: '+ time + '\n'
                                 , reply_markup=send_menu)

    #await state.finish()"""


