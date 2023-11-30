from typing import Dict, Any, List
from sqlalchemy.ext.asyncio import AsyncSession
from model.data.maintenance_record import MaintenanceRecord
from sqlalchemy import update, delete, select, insert

class MaintenanceRecordRepo:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def insert_maintenance_record(self, maintenance_record: Dict) -> MaintenanceRecord:
        try:
            stmt = insert(MaintenanceRecord).values(**maintenance_record)
            await self.db.execute(stmt)
            await self.db.commit()
            return maintenance_record
        except Exception as e:
            print(e)
            return None
    
    async def get_all_maintenance_records(self) -> List[MaintenanceRecord]:
        try:
            stmt = select(MaintenanceRecord)
            result = await self.db.execute(stmt)
            maintenance_records = result.scalars().all()
            return maintenance_records
        except Exception as e:
            print(e)
            return None
    
    async def update_maintenance_record(self, maintenance_record_id: int, maintenance_record: Dict) -> MaintenanceRecord:
        try:
            stmt = update(MaintenanceRecord).where(MaintenanceRecord.id == maintenance_record_id).values(**maintenance_record)
            await self.db.execute(stmt)
            await self.db.commit()
            return maintenance_record
        except Exception as e:
            print(e)
            return None
    
    async def delete_maintenance_record(self, maintenance_record_id: int):
        try:
            stmt = delete(MaintenanceRecord).where(MaintenanceRecord.id == maintenance_record_id)
            await self.db.execute(stmt)
            await self.db.commit()
            return True
        except Exception as e:
            print(e)
            return None
    
    async def get_maintenance_record_by_id(self, maintenance_record_id: int) -> MaintenanceRecord:
        try:
            stmt = select(MaintenanceRecord).where(MaintenanceRecord.id == maintenance_record_id)
            result = await self.db.execute(stmt)
            maintenance_record = result.scalars().first()
            return maintenance_record
        except Exception as e:
            print(e)
            return None
