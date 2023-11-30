from email.mime import image
from pydantic import BaseModel
from typing import Optional, Union
import datetime

'''

class Task(Base):
    __tablename__ = "task"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    start_location: Mapped[str] = mapped_column(String(150), nullable=False)
    end_location: Mapped[str] = mapped_column(String(150), nullable=False)
    start_time: Mapped[str] = mapped_column(Date, nullable=False)
    end_time: Mapped[str] = mapped_column(String(150), nullable=True)
    driver_id: Mapped[int] = mapped_column(Integer, ForeignKey("driver.id"), nullable=False)
    time_spent: Mapped[str] = mapped_column(String(150), nullable=True)
    distance: Mapped[str] = mapped_column(String(150), nullable=True)
    status: Mapped[str] = mapped_column(String(150), nullable=True)
'''

def get_date_now():
    # take full date
    return datetime.datetime.today().strftime('%H:%M:%S')


class TaskCreate(BaseModel):
    start_location: str
    end_location: str
    driver_id: int
    start_time: str = get_date_now()
    time_spent: Optional[str]
    distance: Optional[int]
    


class TaskUpdate(BaseModel):
    start_location: Optional[str]
    end_location: Optional[str]
    driver_id: Optional[int]