'''class Appointment(Base):
    __tablename__ = "appointment"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    vehicle_id: Mapped[int] = mapped_column(Integer, ForeignKey("vehicle.id"), nullable=False)
    license_plate: Mapped[str] = mapped_column(String(150), nullable=False)
    date: Mapped[str] = mapped_column(String(150), nullable=False)
    time: Mapped[str] = mapped_column(String(150), nullable=False)
    maintainance_personnel_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), nullable=False)'''

from pydantic import BaseModel
from typing import Optional, Union
import datetime

def get_date_now():
    # turn it into a string
    return datetime.datetime.today().strftime('%Y-%m-%d')

def get_time_now():
    # take full date
    return datetime.datetime.today().strftime('%H:%M:%S')



class AppointmentCreate(BaseModel):
    vehicle_id: int
    license_plate: str
    date: str = get_date_now()
    time: str = get_time_now()
    maintainance_personnel_id: int

class AppointmentUpdate(BaseModel):
    vehicle_id: Optional[int]
    license_plate: Optional[str]
    date: Optional[str]
    time: Optional[str]
    maintainance_personnel_id: Optional[int]