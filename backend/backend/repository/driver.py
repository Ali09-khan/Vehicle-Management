from typing import Dict, Any, List
from sqlalchemy.ext.asyncio import AsyncSession
from model.data.driver import Driver
from sqlalchemy import update, delete, select, insert

class DriverRepo:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_all_drivers(self) -> List[Driver]:
        try:
            stmt = select(Driver)
            result = await self.db.execute(stmt)
            drivers = result.scalars().all()
            return drivers
        except Exception as e:
            print(e)
            return None
    
    async def create_driver(self, driver: Dict) -> Driver:
        try:
            stmt = insert(Driver).values(**driver)
            await self.db.execute(stmt)
            await self.db.commit()
            return driver
        except Exception as e:
            print(e)
            return None
        
    async def get_driver_by_id(self, driver_id: int) -> Driver:
        try:
            stmt = select(Driver).where(Driver.user_id == driver_id)
            result = await self.db.execute(stmt)
            driver = result.scalars().first()
            return driver
        except Exception as e:
            print(e)
            return None
        
    async def update_driver(self, driver_id: int, driver: Dict) -> Driver:
        try:
            stmt = update(Driver).where(Driver.id == driver_id).values(**driver)
            await self.db.execute(stmt)
            await self.db.commit()
            return driver
        except Exception as e:
            print(e)
            return None
        
    async def delete_driver(self, driver_id: int):
        try:
            stmt = delete(Driver).where(Driver.id == driver_id)
            await self.db.execute(stmt)
            await self.db.commit()
            return True
        except Exception as e:
            print(e)
            return None
        