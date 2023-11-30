import uuid

from fastapi_users import schemas
import datetime
from typing import Union
'''
class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    national_id: Mapped[str] = mapped_column(String(150), nullable=False)
    fname: Mapped[str] = mapped_column(String(150), nullable=False)
    mname: Mapped[str] = mapped_column(String(150), nullable=False)
    lname: Mapped[str] = mapped_column(String(150), nullable=False)
    phone_num: Mapped[str] = mapped_column(String(150), nullable=False) 
    driving_license: Mapped[str] = mapped_column(String(150), nullable=False)
    registration_date: Mapped[Date] = mapped_column(Date, nullable=False)
    
'''
def get_date_now():
    return datetime.datetime.today().strftime('%Y-%m-%d')


class UserRead(schemas.BaseUser[int]):
    role_id: int


class UserCreate(schemas.BaseUserCreate):
    pass

class UserUpdate(schemas.BaseUserUpdate):
    role_id: int