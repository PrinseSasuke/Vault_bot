import sqlite3
from aiogram import  types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import bot, dp
import utils.db_api.quick_commands_request as commands
from handlers.call_back_data import cb
from keyboard import markup_mes_admin
from states import admin_data
import states.data as data_k
admin_id = '5785028847'
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
def admin_menu(ID):
    menu = InlineKeyboardMarkup(row_width=2)
    menu.add(InlineKeyboardButton(text="Принять", callback_data=f"#y{str(ID)}"),
             InlineKeyboardButton(text="Отклонить", callback_data=f'#n{str(ID)}'))
    return menu
@dp.callback_query_handler(cb.filter(action=["send", "application"]), state=data_k.count)
async def send_state(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    data = await state.get_data()
    place = data.get('place')
    date = data.get('date')
    time = data.get('time')
    text = data.get('text')
    count = data.get('count')
    await commands.add_requset(status = 'active', user_name=call.from_user.username, user_id = call.message.from_user.id,
                               place = place, date = date, time = time, text = text, count = count)
    action = callback_data["action"]
    print("fdsfds")
    current_state = await state.get_state()
    print(current_state)
    if current_state is None:
        return

    if action == "send":
        print(call.from_user.id)
        request = await commands.select_request(call.message.from_user.id)
        if request.text:
            await data_k.answer.set()
            await bot.send_message(admin_id, f"Поступила новая заявка от @{request.user_name}\n" +
                                   f"ДАТА: {request.date}\n" +
                                   f"ЗАЛ: {request.place}\n" +
                                   f"ВРЕМЯ: {request.time}\n"+
                                   f"Кол-во мест: '{request.count}\n"+
                                   f"Сообщение от пользователя: {request.text}", reply_markup=admin_menu(call.from_user.id))


        else:
            await admin_data.answer.set()
            await bot.send_message(admin_id, f"Поступила новая заявка от @{request.user_name}\n"+
                                   f"ДАТА: {request.date}\n"+
                                   f"ЗАЛ: {request.place}\n"+
                                   f"ВРЕМЯ: {request.time}\n"+
                                   f"Кол-во мест: {request.count}\n",reply_markup=admin_menu(call.from_user.id))
        await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text="Заявка отправлена, ожидайте")
        await data_k.answer.set()
        print(await state.get_state())
@dp.callback_query_handler(text_contains="#")
async def access(call: types.CallbackQuery, state: FSMContext):  # Обработка заявки
    print(await state.get_state())
    temp = [call.data[1:2], call.data[2:]]
    print(temp)
    await state.update_data(user_id = temp[1])
    if temp[0] == "y":
        """
        await bot.edit_message_text(chat_id=admin_id, message_id=call.message.message_id, text="Вы приняли заявку")
        await bot.send_message(temp[1],text =f"ДАТА: {request.date}\n"+
                               f"ЗАЛ: {request.place}\n"+
                               f"ВРЕМЯ: {request.time}\n"+"Заявка принята")
        """
        await state.update_data(answer = 'y')
        print('sadasdasdasz')
        await bot.edit_message_text(chat_id=admin_id, message_id=call.message.message_id, text="Добавить сообщение", reply_markup=markup_mes_admin)
        #await commands.delete_request(call.message.from_user.id)
    elif temp[0] == "n":
        """await bot.edit_message_text(chat_id=admin_id, message_id=call.message.message_id, text="Вы отклонили заявку")
        await bot.send_message(temp[1], 'Извините, заявка отклонена')
        await commands.delete_request(call.message.from_user.id)"""
        await state.update_data(answer='n')
        await bot.edit_message_text(chat_id=admin_id, message_id=call.message.message_id, text="Добавить сообщение", reply_markup=markup_mes_admin)
    #await call.answer()
@dp.callback_query_handler(text=['yes', 'no'], state='*')
async def access(call: types.CallbackQuery, state: FSMContext):  # Обработка заявки
    print(call.data)
    print('dfdsfdsfsdweqweqw')
    if call.data == "yes":
        """
        await bot.edit_message_text(chat_id=admin_id, message_id=call.message.message_id, text="Вы приняли заявку")
        await bot.send_message(temp[1],text =f"ДАТА: {request.date}\n"+
                               f"ЗАЛ: {request.place}\n"+
                               f"ВРЕМЯ: {request.time}\n"+"Заявка принята")
        """
        await admin_data.text.set()
        print(await state.get_state())
        #await commands.delete_request(call.message.from_user.id)
    elif call.data == "no":
        """await bot.edit_message_text(chat_id=admin_id, message_id=call.message.message_id, text="Вы отклонили заявку")
        await bot.send_message(temp[1], 'Извините, заявка отклонена')
        await commands.delete_request(call.message.from_user.id)"""
        await state.update_data(answer='n')
        await bot.edit_message_text(chat_id=admin_id, message_id=call.message.message_id, text="Добавить сообщение", reply_markup=markup_mes_admin)
