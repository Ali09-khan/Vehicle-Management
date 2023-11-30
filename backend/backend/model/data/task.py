from sqlalchemy import Time, Column, ForeignKey, Integer, String, Float, Date, MetaData
from sqlalchemy.orm import relationship, Mapped, mapped_column
from db_config.db_connection import Base


class Task(Base):
    __tablename__ = "task"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    start_location: Mapped[str] = mapped_column(String(150), nullable=False)
    end_location: Mapped[str] = mapped_column(String(150), nullable=False)
    start_time: Mapped[str] = mapped_column(String(150), nullable=False)
    end_time: Mapped[str] = mapped_column(String(150), nullable=True)
    driver_id: Mapped[int] = mapped_column(Integer, ForeignKey("driver.id"), nullable=False)
    time_spent: Mapped[str] = mapped_column(String(150), nullable=True)
    distance: Mapped[int] = mapped_column(Integer, nullable=True)
    status: Mapped[str] = mapped_column(String(150), nullable=True)