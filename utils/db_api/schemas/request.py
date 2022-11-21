from utils.db_api.db_gino import TimedBaseModel
from sqlalchemy import Column, BigInteger, String, sql, Float, ForeignKey, Sequence

class Request(TimedBaseModel):
    __tablename__ = 'requests'
    user_name = Column(String(100))
    request_id = Column(BigInteger, Sequence("request_id_seq", start=1, optional=True), primary_key = True)
    status = Column(String(30))
    user_id = Column(BigInteger)
    place = Column(String(30))
    date = Column(String(30))
    time = Column(String(30))
    count = Column(String(1))
    text = Column(String(150))
    query:sql.select