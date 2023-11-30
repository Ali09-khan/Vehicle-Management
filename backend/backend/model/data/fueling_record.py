from sqlalchemy import Time, Column, ForeignKey, Integer, String, Float, Date, MetaData
from sqlalchemy.orm import relationship, Mapped, mapped_column
from db_config.db_connection import Base


class FuelingRecord(Base):
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
