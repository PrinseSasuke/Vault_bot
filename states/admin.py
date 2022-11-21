from  aiogram.dispatcher.filters.state import StatesGroup, State
class admin_data(StatesGroup):
    answer = State()
    text = State()
    user_id = State()