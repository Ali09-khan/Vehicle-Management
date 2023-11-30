from sqlalchemy import Time, Column, ForeignKey, Integer, String, Float, Date, MetaData
from sqlalchemy.orm import relationship, Mapped, mapped_column
from db_config.db_connection import Base

class Vehicle(Base):
    __tablename__ = "vehicle"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    model: Mapped[str] = mapped_column(String(150), nullable=False)
    license_plate: Mapped[str] = mapped_column(String(150), nullable=False)
    sitting_capacity: Mapped[int] = mapped_column(Integer, nullable=False)
    driver_id: Mapped[int] = mapped_column(Integer, ForeignKey("driver.id"), nullable=False)

    appointment = relationship("Appointment", backref="vehicle")
    maintenance_record = relationship("MaintenanceRecord", backref="vehicle")
    fueling_record = relationship("FuelingRecord", backref="vehicle")