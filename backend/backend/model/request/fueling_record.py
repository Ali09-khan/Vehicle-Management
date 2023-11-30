'''class FuelingRecord(Base):
    __tablename__ = "fueling_record"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    vehicle_id: Mapped[int] = mapped_column(Integer, ForeignKey("vehicle.id"), nullable=False)
    driver_id: Mapped[int] = mapped_column(Integer, ForeignKey("driver.id"), nullable=False)
    car_plate_info: Mapped[str] = mapped_column(String(150), nullable=False)
    date_and_time: Mapped[str] = mapped_column(String(150), nullable=False)
    amount_of_fuel: Mapped[int] = mapped_column(Integer, nullable=False)
    fuel_type: Mapped[str] = mapped_column(String(150), nullable=False)
    cost: Mapped[int] = mapped_column(Integer, nullable=False)
    gas_station_name: Mapped[str] = mapped_column(String(150), nullable=False)
    fueling_personnel_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), nullable=False)
    driver_image: Mapped[str] = mapped_column(String(150), nullable=False)
    fuel_levels_before: Mapped[int] = mapped_column(Integer, nullable=False)
    fuel_levels_after: Mapped[int] = mapped_column(Integer, nullable=False)
    milage: Mapped[int] = mapped_column(Integer, nullable=False)
'''

from pydantic import BaseModel
from typing import Optional, Union
import datetime

def get_date_now():
    # turn it into a string
    return datetime.datetime.today().strftime('%Y-%m-%d')

class FuelingRecordCreate(BaseModel):
    vehicle_id: int
    driver_id: int
    car_plate_info: str
    date_and_time: str = get_date_now()
    amount_of_fuel: int
    fuel_type: str
    cost: int
    gas_station_name: str
    fueling_personnel_id: int
    driver_image: str
    fuel_levels_before: int
    fuel_levels_after: int
    milage: int

class FuelingRecordUpdate(BaseModel):
    vehicle_id: Optional[int]
    driver_id: Optional[int]
    car_plate_info: Optional[str]
    date_and_time: Optional[str]
    amount_of_fuel: Optional[int]
    fuel_type: Optional[str]
    cost: Optional[int]
    gas_station_name: Optional[str]
    fueling_personnel_id: Optional[int]
    driver_image: Optional[str]
    fuel_levels_before: Optional[int]
    fuel_levels_after: Optional[int]
    milage: Optional[int]