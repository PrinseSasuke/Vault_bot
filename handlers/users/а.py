import sqlite3
from aiogram import executor, types, Bot, Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.contrib.fsm_storage.memory import MemoryStorage


# __________________________Данные бота__________________________
admin_id = 123213# Id админа
token = "12354236:AAF_uрhljfghrerg__ViEmj-9OccIDZVZQlE"  # Токен бота
chat_link = "https://yandex.com"  # Ссылка на чат
bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
# __________________________Вопросы__________________________
question_1 = "Сколько вам лет?"
question_2 = "Сколько времени готовы уделять работе?"
question_3 = "Был ли у вас опыт в похожем проекте?"
# __________________________Отображение вопросов у админа__________________________
admin_question_1 = "Возраст"
admin_question_2 = "Сколько готов уделять времени"
admin_question_3 = "Был ли опыт"
# _________________________________________________________


# __________________________Действие при старте бота__________________________
async def on_startup(_):
    print("Bot Started")
# _________________________________________________________


# __________________________Действие с БД__________________________
class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        print("The database is connected successfully")

    def add_user(self, ID, username):
        with self.connection:
            try:
                self.cursor.execute("INSERT INTO 'user' VALUES (?, ?, ?, ?, ?)", (ID, "null", "null", "null", username))
            except: pass

    def add_client(self, ID):
        with self.connection:
            try:
                self.cursor.execute("INSERT INTO 'client' VALUES (?)", (ID,))
            except: pass

    def update_user_data(self, ID, a1, a2, a3):
        with self.connection:
            self.cursor.execute("UPDATE 'user' SET answer1 = ?, answer2 = ?, answer3 = ? WHERE user_id = ?", (a1, a2, a3, ID))

    def get_user_data(self, ID):
        with self.connection:
            return self.cursor.execute("SELECT * FROM 'user' WHERE user_id = ?", (ID,)).fetchmany()[0]

    def delete_zayavka(self, ID):
        with self.connection:
            return self.cursor.execute("DELETE FROM 'user' WHERE user_id = ?", (ID,))

    def client_exists(self, ID):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'user' WHERE user_id = ?", (ID,)).fetchmany(1)
            if not bool(len(result)):
                return False
            else: return True

    def confirmed_user(self, ID):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'client' WHERE user_id = ?", (ID,)).fetchmany(1)
            if not bool(len(result)):
                return False
            else: return True
# _________________________________________________________

# __________________________Кнопки__________________________
cb = CallbackData("fabnum", "action")

main_menu = InlineKeyboardMarkup(row_width=1)
main_menu.add(InlineKeyboardButton(text='Подать заявку', callback_data=cb.new(action='start_answer')))

send_menu = InlineKeyboardMarkup(row_width=2)
send_menu.add(InlineKeyboardButton(text="Отправить", callback_data=cb.new(action="send")),
              InlineKeyboardButton(text="Заполнить заново", callback_data=cb.new(action='application')))


def admin_menu(ID):
    menu = InlineKeyboardMarkup(row_width=2)
    menu.add(InlineKeyboardButton(text="Принять", callback_data=f"#y{str(ID)}"),
             InlineKeyboardButton(text="Отклонить", callback_data=f'#n{str(ID)}'))
    return menu
# _________________________________________________________

# __________________________Подключаем БД__________________________
db = Database("data.db")
# _________________________________________________________


class get_answer(StatesGroup):
    answer1 = State()
    answer2 = State()
    answer3 = State()


# ____________________________________________________
# @dp.message_handlers(commands=["start"])
async def command_start(message: types.Message):  # Действие при /start
    if message.from_user.username is not None:
        if db.confirmed_user(message.from_user.id):
            await bot.send_message(message.from_user.id, " Вы уже приняты ")
        else:
            if db.client_exists(message.from_user.id):
                await bot.send_message(message.from_user.id, "Вы уже подавали заявку ")
            else:
                await bot.send_message(message.from_user.id,
                                       "Добро пожаловать\n \nПрием заявок в Our Team \n \nПодавай заявку",  # Приветственное сообщение
                                       reply_markup=main_menu)
    else:
        await bot.send_message(message.from_user.id, "У вас не установлен <b>username</b>(имя пользователя)\n\nУстановите его и напишите /start", parse_mode=types.ParseMode.HTML)


# @dp.callback_query_handlers(cb.filter(action=["send", "application"]), state="*")
async def send_state(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    action = callback_data["action"]
    current_state = await state.get_state()
    if current_state is None:
        return
    if action == "send":
        await bot.send_message(admin_id, f"Поступила новая заявка от @{str(db.get_user_data(call.from_user.id)[4])}\n"
                                         f"{admin_question_1}: <b>{str(db.get_user_data(call.from_user.id)[1])}</b>\n"
                                         f"{admin_question_2}: <b>{str(db.get_user_data(call.from_user.id)[2])}</b>\n"
                                         f"{admin_question_3}: <b>{str(db.get_user_data(call.from_user.id)[3])}</b>", parse_mode=types.ParseMode.HTML, reply_markup=admin_menu(call.from_user.id))
        await bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.message_id, text="Заявка отправлена, ожидайте")
        await state.finish()
    if action == "application":
        db.delete_zayavka(call.from_user.id)
        await state.finish()
        await command_start(call)
    await call.answer()


# @dp.callback_query_handler(text_contains="#")
async def access(call: types.CallbackQuery):  # Обработка заявки
    temp = [call.data[1:2], call.data[2:]]
    if temp[0] == "y":
        db.add_client(temp[1])
        db.delete_zayavka(temp[1])
        await bot.edit_message_text(chat_id=admin_id, message_id=call.message.message_id, text="Вы приняли заявку")
        await bot.send_message(temp[1], f'Поздравляю, вы приняты в нашу команду \n \n'
                                        f' Ссылка для вступления в чат: {chat_link} \n \n'
                                        f' <b>ЧИТАЙТЕ ВСЕ МАНУАЛЫ В ЗАКРЕПЕ </b>', disable_web_page_preview=True, parse_mode=types.ParseMode.HTML)
    elif temp[0] == "n":
        await bot.edit_message_text(chat_id=admin_id, message_id=call.message.message_id, text="Вы отклонили заявку")
        await bot.send_message(temp[1], 'Извините, вы нам не подходите ')

    await call.answer()


# @dp.callback_query_handlers(cb.filter(action=["start_answer"]))
async def start_state(call: types.CallbackQuery, callback_data: dict):  # Первый вопрос
    action = callback_data["action"]
    if action == "start_answer":
        db.add_user(call.from_user.id, call.from_user.username)
        await bot.send_message(call.from_user.id, f"Ответьте на несколько вопросов:\n1) <b>{question_1}</b>", parse_mode=types.ParseMode.HTML)
        await get_answer.answer1.set()


# @dp.message_handlers(state=get_answer.answer1)
async def answer1(message: types.Message, state: FSMContext):  # Второй вопрос
    async with state.proxy() as data:
        data["answer1"] = message.text
    await bot.send_message(message.from_user.id, f'2) <b>{question_2}</b>', parse_mode=types.ParseMode.HTML)
    await get_answer.next()


# @dp.message_handlers(state=get_answer.answer2)
async def answer2(message: types.Message, state: FSMContext):  # Третий вопрос
    async with state.proxy() as data:
        data["answer2"] = message.text
    await bot.send_message(message.from_user.id, f'3) <b>{question_3}</b>', parse_mode=types.ParseMode.HTML)
    await get_answer.next()


# @dp.message_handlers(state=get_answer.answer3)
async def answer3(message: types.Message, state: FSMContext):  # Отображение ответов на вопросы
    async with state.proxy() as data:
        data["answer3"] = message.text
    await bot.send_message(message.from_user.id, f'Ответы на наши вопросы:\n\n'
                                                 f'1) <b>{data["answer1"]}</b>\n'
                                                 f'2) <b>{data["answer2"]}</b>\n'
                                                 f'3) <b>{data["answer3"]}</b>', parse_mode=types.ParseMode.HTML, reply_markup=send_menu)
    db.update_user_dat
