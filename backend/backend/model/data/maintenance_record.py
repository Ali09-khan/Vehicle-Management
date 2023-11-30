from sqlalchemy import Time, Column, ForeignKey, Integer, String, Float, Date, MetaData
from sqlalchemy.orm import relationship, Mapped, mapped_column
from db_config.db_connection import Base

class MaintenanceRecord(Base):
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
    