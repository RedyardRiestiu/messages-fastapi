import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Messages(Base):
    __tablename__: str = 'messages'

    id = sa.Column(sa.Integer, primary_key=True)
    date = sa.Column(sa.Date)
    payload = sa.Column(sa.String)                  #содержимое сообщения от пользователя
    number = sa.Column(sa.Integer)