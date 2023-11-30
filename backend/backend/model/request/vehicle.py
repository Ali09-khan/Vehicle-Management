'''class Vehicle(Base):
    __tablename__ = "vehicle"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    model: Mapped[str] = mapped_column(String(150), nullable=False)
    license_plate: Mapped[str] = mapped_column(String(150), nullable=False)
    sitting_capacity: Mapped[int] = mapped_column(Integer, nullable=False)
    driver_id: Mapped[int] = mapped_column(Integer, ForeignKey("driver.id"), nullable=False)'''

from pydantic import BaseModel
from typing import Optional, Union


class VehicleCreate(BaseModel):
    model: str
    license_plate: str
    sitting_capacity: int
    driver_id: int

class VehicleUpdate(BaseModel):
    model: Optional[str]
    license_plate: Optional[str]
    sitting_capacity: Optional[int]
    driver_id: Optional[int]