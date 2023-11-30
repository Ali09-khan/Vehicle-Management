from email.mime import image
from pydantic import BaseModel
from typing import Optional, Union
import datetime

def get_date_now():
    # turn it into a string
    return datetime.datetime.today().strftime('%Y-%m-%d')

class DriverCreate(BaseModel):
    fname: str
    mname: str
    lname: str
    phone_num: str
    driving_license: str
    registration_date: str = get_date_now()
    user_id: int

class DriverUpdate(BaseModel):
    national_id: Optional[str]
    fname: Optional[str]
    mname: Optional[str]
    lname: Optional[str]
    phone_num: Optional[str]
    driving_license: Optional[str]
    role_id: Optional[int]
