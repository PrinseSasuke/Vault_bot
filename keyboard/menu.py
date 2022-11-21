from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
markup_start = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [InlineKeyboardButton(text='БРОНЬ', callback_data='reserve'),
                                   InlineKeyboardButton(text='ИНФО', callback_data='info')
                                   ]])
markup_place = InlineKeyboardMarkup(row_width=4,
                              inline_keyboard=[
                                  [InlineKeyboardButton(text='ОСНОВНОЙ', callback_data='main')

                                   ]],)
markup_place.row(InlineKeyboardButton(text='VIP👑', callback_data='vip'))
markup_place.row(InlineKeyboardButton(text='ULTRA VIP👑', callback_data='ultra_vip'))
markup_place.row(InlineKeyboardButton(text='PS4 V44🎮', callback_data='ps4'))
markup_hours = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [InlineKeyboardButton(text='1', callback_data='1'),
                                   InlineKeyboardButton(text='2', callback_data='2'),
                                   InlineKeyboardButton(text='3', callback_data='3'),
                                   InlineKeyboardButton(text='4', callback_data='4'),
                                   InlineKeyboardButton(text='5', callback_data='5'),
                                   InlineKeyboardButton(text='6', callback_data='6')
                                   ]])
markup_hours.row(InlineKeyboardButton(text='7', callback_data='7'),
                 InlineKeyboardButton(text='8', callback_data='8'),
                 InlineKeyboardButton(text='9', callback_data='9'),
                 InlineKeyboardButton(text='10', callback_data='10'),
                 InlineKeyboardButton(text='11', callback_data='11'),
                 InlineKeyboardButton(text='12', callback_data='12'))
markup_time = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [InlineKeyboardButton(text='0:00', callback_data='0:00'),
                                   InlineKeyboardButton(text='1:00', callback_data='1:00'),
                                   InlineKeyboardButton(text='2:00', callback_data='2:00'),
                                   InlineKeyboardButton(text='3:00', callback_data='3:00'),
                                   InlineKeyboardButton(text='4:00', callback_data='4:00'),
                                   InlineKeyboardButton(text='5:00', callback_data='5:00'),
                                   InlineKeyboardButton(text='6:00', callback_data='6:00')
                                   ]])
markup_time.row(InlineKeyboardButton(text='7:00', callback_data='7:00'),
                                   InlineKeyboardButton(text='8:00', callback_data='8:00'),
                                   InlineKeyboardButton(text='9:00', callback_data='9:00'),
                                   InlineKeyboardButton(text='10:00', callback_data='10:00'),
                                   InlineKeyboardButton(text='11:00', callback_data='11:00'),
                                   InlineKeyboardButton(text='12:00', callback_data='12:00'))
markup_time.row(InlineKeyboardButton(text='13:00', callback_data='13:00'),
                InlineKeyboardButton(text='14:00', callback_data='14:00'),
                InlineKeyboardButton(text='15:00', callback_data='15:00'),
                InlineKeyboardButton(text='16:00', callback_data='16:00'),
                InlineKeyboardButton(text='17:00', callback_data='17:00'),
                InlineKeyboardButton(text='18:00', callback_data='18:00'))

markup_time.row(InlineKeyboardButton(text='19:00', callback_data='19:00'),
                InlineKeyboardButton(text='20:00', callback_data='20:00'),
                InlineKeyboardButton(text='21:00', callback_data='21:00'),
                InlineKeyboardButton(text='22:00', callback_data='22:00'),
                InlineKeyboardButton(text='23:00', callback_data='23:00'))
def admin_menu(request_id):
    menu = InlineKeyboardMarkup(row_width=2)
    menu.add(InlineKeyboardButton(text="Принять", callback_data=f"#y{str(request_id)}"),
             InlineKeyboardButton(text="Отклонить", callback_data=f'#n{str(request_id)}'))
    return menu
markup_count = InlineKeyboardMarkup(row_width=4,
                              inline_keyboard=[
                                  [InlineKeyboardButton(text='1', callback_data='1')

                                   ]],)
markup_count.row(InlineKeyboardButton(text='2', callback_data='2'))
markup_count.row(InlineKeyboardButton(text='3', callback_data='3'))
markup_count.row(InlineKeyboardButton(text='4', callback_data='4'))
markup_count.row(InlineKeyboardButton(text='5', callback_data='5'))

markup_mes_admin = InlineKeyboardMarkup(row_width=4,
                              inline_keyboard=[
                                  [InlineKeyboardButton(text='Да', callback_data='yes'),
                                   InlineKeyboardButton(text='Нет', callback_data='no')
                                   ]],)