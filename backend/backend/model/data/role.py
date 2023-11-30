from sqlalchemy import Time, Column, ForeignKey, Integer, String, Float, Date, MetaData
from sqlalchemy.orm import relationship, Mapped, mapped_column
from db_config.db_connection import Base

class Role(Base):
    __tablename__ = "role"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)

    user = relationship("User", back_populates="role")