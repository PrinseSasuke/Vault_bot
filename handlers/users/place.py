from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from states import data
from keyboard import markup_start, markup_place
#Process place
@dp.callback_query_handler(state = data.place)
async def place(call: types.CallbackQuery, state:FSMContext):
    from datetime import datetime, timedelta
    current_date = datetime.now().date()
    await state.update_data(place=call.data)
    await call.message.edit_text("Выбери день:")
    markup_place = InlineKeyboardMarkup(row_width=4,
                                        inline_keyboard=[
                                            [InlineKeyboardButton(text=str(current_date), callback_data='today'),
                                             ]])
    markup_place.row(InlineKeyboardButton(text=str(current_date + timedelta(days=1)), callback_data='tommorow'))
    markup_place.row(InlineKeyboardButton(text=str(current_date + timedelta(days=2)), callback_data='tommorow_1'))
    markup_place.row(InlineKeyboardButton(text=str(current_date + timedelta(days=3)), callback_data='tommorow_2'))
    await call.message.edit_reply_markup(reply_markup=markup_place)
    await data.date.set() #date.py
