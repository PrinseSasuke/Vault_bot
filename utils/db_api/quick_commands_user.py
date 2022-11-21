"""from utils.db_api.schemas.user import User
from asyncpg import UniqueViolationError
from utils.db_api.db_gino import db
async def add_user(user_id: int,  username:str, status:str):
    try:
        user = User(user_id = user_id, username = username, status = status)
        await user.create()
    except UniqueViolationError:
        print("Пользователь не добавлен")
async def select_all_users():
    users = await User.query.gino.all()
    return users
async def select_user(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user
"""