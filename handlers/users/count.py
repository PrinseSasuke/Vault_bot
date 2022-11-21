from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from states import data
from handlers.call_back_data import cb
from keyboard import markup_time
send_menu = InlineKeyboardMarkup(row_width=2)
send_menu.add(InlineKeyboardButton(text="Отправить", callback_data=cb.new(action="send")),
                InlineKeyboardButton(text="Заполнить заново", callback_data="resend"),
                InlineKeyboardButton(text="Добавить сообщение", callback_data="mail"))
@dp.callback_query_handler(text = ['1','2','3','4','5'], state = data.count)
async def reserve(call: types.CallbackQuery, state:FSMContext):
    await state.update_data(count = call.data)
    data = await state.get_data()
    place = data.get('place')
    date = data.get('date')
    time = data.get('time')
    count = data.get('count')
    print(data)
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
                                 'ВРЕМЯ: '+ time + '\n'+
                                 'КОЛ-ВО МЕСТ:'+count
                                 , reply_markup=send_menu)
