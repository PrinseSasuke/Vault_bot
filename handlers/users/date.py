from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from states import data
from keyboard import markup_time
@dp.callback_query_handler(text = 'today', state = data.date)
async def reserve(call: types.CallbackQuery, state:FSMContext):
    from datetime import datetime, timedelta
    current_date = datetime.now().date()
    await state.update_data(date = str(current_date))
    await call.message.edit_text("Выбери время:")
    await call.message.edit_reply_markup(markup_time)
    await data.time.set()
@dp.callback_query_handler(text = 'tommorow', state = data.date)
async def reserve(call: types.CallbackQuery, state:FSMContext):
    from datetime import datetime, timedelta
    current_date = datetime.now().date() + timedelta(days = 1)
    await state.update_data(date = str(current_date))
    await call.message.edit_text("Выбери количество часов:")
    await call.message.edit_reply_markup(markup_time)
    await data.time.set()
@dp.callback_query_handler(text = 'tommorow_1', state = data.date)
async def reserve(call: types.CallbackQuery, state:FSMContext):
    from datetime import datetime, timedelta
    current_date = datetime.now().date() + timedelta(days = 2)
    await state.update_data(date = str(current_date))
    await call.message.edit_text("Выбери количество часов:")
    await call.message.edit_reply_markup(markup_time)
    await data.time.set()
@dp.callback_query_handler(text = 'tommorow_2', state = data.date)
async def reserve(call: types.CallbackQuery, state:FSMContext):
    from datetime import datetime, timedelta
    current_date = datetime.now().date() + timedelta(days = 3)
    await state.update_data(date = str(current_date))
    await call.message.edit_text("Выбери время:")
    await call.message.edit_reply_markup(markup_time)
    await data.time.set()