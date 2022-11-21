from  aiogram.dispatcher.filters.state import StatesGroup, State
class data(StatesGroup):
    place = State()
    date = State()
    time = State()
    text = State()
    count = State()
    answer = State()
