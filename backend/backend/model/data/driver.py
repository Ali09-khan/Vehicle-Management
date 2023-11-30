from sqlalchemy import Time, Column, ForeignKey, Integer, String, Float, Date, MetaData
from sqlalchemy.orm import relationship, Mapped, mapped_column
from db_config.db_connection import Base


'''
sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('fname', sa.String(length=150), nullable=False),
    sa.Column('mname', sa.String(length=150), nullable=False),
    sa.Column('lname', sa.String(length=150), nullable=False),
    sa.Column('phone_num', sa.String(length=150), nullable=False),
    sa.Column('driving_license', sa.String(length=150), nullable=False),
    sa.Column('registration_date', sa.Date(), nullable=False),
'''

class Driver(Base):
    __tablename__ = "driver"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), nullable=False)
    fname: Mapped[str] = mapped_column(String(150), nullable=False)
    mname: Mapped[str] = mapped_column(String(150), nullable=False)
    lname: Mapped[str] = mapped_column(String(150), nullable=False)
    phone_num: Mapped[str] = mapped_column(String(150), nullable=False)
    driving_license: Mapped[str] = mapped_column(String(150), nullable=False)
    registration_date: Mapped[str] = mapped_column(String(150), nullable=False)

    task = relationship("Task", backref="driver")
    vehicle = relationship("Vehicle", backref="driver")
    fueling_record = relationship("FuelingRecord", backref="driver")