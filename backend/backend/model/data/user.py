from sqlalchemy import Time, Column, ForeignKey, Integer, String, Float, Date, MetaData
from sqlalchemy.orm import relationship, Mapped, mapped_column
from db_config.db_connection import Base
from fastapi_users.db import SQLAlchemyBaseUserTable


class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey("role.id"))

    role = relationship("Role", back_populates="user")
    driver = relationship("Driver", backref="user")
    appointment = relationship("Appointment", backref="user")
    maintenance_record = relationship("MaintenanceRecord", backref="user")
    fueling_record = relationship("FuelingRecord", backref="user")