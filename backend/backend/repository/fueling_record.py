from typing import Dict, Any, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update, delete, select, insert
from model.data.fueling_record import FuelingRecord

class FuelingRecordRepo:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def insert_fueling_record(self, fueling_record: Dict) -> FuelingRecord:
        try:
            stmt = insert(FuelingRecord).values(**fueling_record)
            await self.db.execute(stmt)
            await self.db.commit()
            return fueling_record
        except Exception as e:
            print(e)
            return None
    
    async def get_all_fueling_records(self) -> List[FuelingRecord]:
        try:
            stmt = select(FuelingRecord)
            result = await self.db.execute(stmt)
            fueling_records = result.scalars().all()
            return fueling_records
        except Exception as e:
            print(e)
            return None
    
    async def update_fueling_record(self, fueling_record_id: int, fueling_record: Dict) -> FuelingRecord:
        try:
            stmt = update(FuelingRecord).where(FuelingRecord.id == fueling_record_id).values(**fueling_record)
            await self.db.execute(stmt)
            await self.db.commit()
            return fueling_record
        except Exception as e:
            print(e)
            return None
    
    async def delete_fueling_record(self, fueling_record_id: int):
        try:
            stmt = delete(FuelingRecord).where(FuelingRecord.id == fueling_record_id)
            await self.db.execute(stmt)
            await self.db.commit()
            return True
        except Exception as e:
            print(e)
            return None
    
    async def get_fueling_record_by_id(self, fueling_record_id: int) -> FuelingRecord:
        try:
            stmt = select(FuelingRecord).where(FuelingRecord.id == fueling_record_id)
            result = await self.db.execute(stmt)
            fueling_record = result.scalars().first()
            return fueling_record
        except Exception as e:
            print(e)
            return None
        
    async def get_fueling_record_by_driver_id(self, driver_id: int) -> FuelingRecord:
        try:
            stmt = select(FuelingRecord).where(FuelingRecord.driver_id == driver_id)
            result = await self.db.execute(stmt)
            fueling_record = result.scalars().first()
            return fueling_record
        except Exception as e:
            print(e)
            return None
        
