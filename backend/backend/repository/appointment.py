from typing import Dict, Any, List
from sqlalchemy.ext.asyncio import AsyncSession
from model.data.appointment import Appointment
from sqlalchemy import update, delete, select, insert

class AppointmentRepo:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def insert_appointment(self, appointment: Dict) -> Appointment:
        try:
            stmt = insert(Appointment).values(**appointment)
            await self.db.execute(stmt)
            await self.db.commit()
            return appointment
        except Exception as e:
            print(e)
            return None
        
    async def get_all_appointments(self) -> List[Appointment]:
        try:
            stmt = select(Appointment)
            result = await self.db.execute(stmt)
            appointments = result.scalars().all()
            return appointments
        except Exception as e:
            print(e)
            return None
        
    async def update_appointment(self, appointment_id: int, appointment: Dict) -> Appointment:
        try:
            stmt = update(Appointment).where(Appointment.id == appointment_id).values(**appointment)
            await self.db.execute(stmt)
            await self.db.commit()
            return appointment
        except Exception as e:
            print(e)
            return None
        
    async def delete_appointment(self, appointment_id: int):
        try:
            stmt = delete(Appointment).where(Appointment.id == appointment_id)
            await self.db.execute(stmt)
            await self.db.commit()
            return True
        except Exception as e:
            print(e)
            return None
        
    async def get_appointment_by_id(self, appointment_id: int) -> Appointment:
        try:
            stmt = select(Appointment).where(Appointment.id == appointment_id)
            result = await self.db.execute(stmt)
            appointment = result.scalars().first()
            return appointment
        except Exception as e:
            print(e)
            return None
