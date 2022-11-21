from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from states import data
from keyboard import markup_start, markup_place
from handlers.call_back_data import cb
send_menu = InlineKeyboardMarkup(row_width=2)
send_menu.add(InlineKeyboardButton(text="Отправить", callback_data=cb.new(action="send")),
                InlineKeyboardButton(text="Заполнить заново", callback_data="resend"))
@dp.callback_query_handler(state = "*", text = 'mail')
async def mail(call: types.CallbackQuery):
    await call.message.edit_text("Введите текст: ")
    await data.text.set()
@dp.message_handler(state = data.text)
async def mess(message: types.Message, state:FSMContext):
    text = message.text
    await state.update_data(text = text)
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
    await message.answer('Твоя заявка: \n'+
                                 'ЗАЛ: ' + place_text + '\n'+
                                 'ДАТА: '+ date + '\n'+
                                 'ВРЕМЯ: '+ time + '\n'
                                 , reply_markup=send_menu)


