from sqlalchemy import Column, BigInteger, String

from models import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    user_id = Column(BigInteger, nullable=False, autoincrement=False, primary_key=True)
    name = Column(String(length=60), nullable=True)
    guruh = Column(String(length=20), nullable=True)
    number = Column(String(length=20), nullable=True)

    def __repr__(self):
        return f'{self.user_id}'
