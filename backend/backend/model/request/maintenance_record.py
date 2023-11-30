'''class MaintenanceRecord(Base):
    __tablename__ = "maintenance_record"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    vehicle_id: Mapped[int] = mapped_column(Integer, ForeignKey("vehicle.id"), nullable=False)
    mainteneance_personnel_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), nullable=False)
    maintenance_description: Mapped[str] = mapped_column(String(150), nullable=False)
    milage: Mapped[int] = mapped_column(Integer, nullable=False)
    date_and_time: Mapped[str] = mapped_column(String(150), nullable=False)
    status: Mapped[str] = mapped_column(String(150), nullable=False)
    part_numbers: Mapped[int] = mapped_column(Integer, nullable=False)
    photo: Mapped[str] = mapped_column(String(150), nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    '''
from email.mime import image
from pydantic import BaseModel
from typing import Optional, Union
import datetime

def get_date_now():
    # take full date
    return datetime.datetime.today().strftime('%Y-%m-%d, %H:%M:%S')

class MaintenanceRecordCreate(BaseModel):
    vehicle_id: int
    mainteneance_personnel_id: int
    maintenance_description: str
    milage: int
    date_and_time: str = get_date_now()
    part_numbers: int
    photo: str
    price: int

class MaintenanceRecordUpdate(BaseModel):
    vehicle_id: Optional[int]
    mainteneance_personnel_id: Optional[int]
    maintenance_description: Optional[str]
    milage: Optional[int]
    date_and_time: Optional[str]
    status: Optional[str]
    part_numbers: Optional[int]
    photo: Optional[str]
    price: Optional[int]