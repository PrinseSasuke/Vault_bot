from utils.db_api.schemas.request import Request
from asyncpg import UniqueViolationError
from utils.db_api.db_gino import db
from sqlalchemy import delete
async def add_requset(status:str, user_name:str, user_id:str, place: str, date: str, time: str, count:str, text = None):
    try:
        request = Request(status = status, user_name = user_name, user_id = user_id, place = place, date = date, time = time, text = text, count = count)
        await request.create()
    except UniqueViolationError:
        print("Заявка не добавлена")
async def select_all_requsets():
    users = await Request.query.gino.all()
    return users
async def select_request(user_id):
    requests = await Request.query.where(Request.user_id == user_id).gino.all()
    request = requests[0]
    return request
async def delete_request(user_id):
    request = await select_request(user_id)
    await request.delete()