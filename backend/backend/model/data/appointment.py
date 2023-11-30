from sqlalchemy import Time, Column, ForeignKey, Integer, String, Float, Date, MetaData
from sqlalchemy.orm import relationship, Mapped, mapped_column
from db_config.db_connection import Base

class Appointment(Base):
    __tablename__ = "appointment"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    vehicle_id: Mapped[int] = mapped_column(Integer, ForeignKey("vehicle.id"), nullable=False)
    license_plate: Mapped[str] = mapped_column(String(150), nullable=False)
    date: Mapped[str] = mapped_column(String(150), nullable=False)
    time: Mapped[str] = mapped_column(String(150), nullable=False)
    maintainance_personnel_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), nullable=False)