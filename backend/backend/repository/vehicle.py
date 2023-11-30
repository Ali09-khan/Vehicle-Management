from typing import Dict, Any, List
from sqlalchemy.ext.asyncio import AsyncSession
from model.data.vehicle import Vehicle
from sqlalchemy import update, delete, select, insert


class VehicleRepo:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def insert_vehicle(self, vehicle: Dict) -> Vehicle:
        try:
            stmt = insert(Vehicle).values(**vehicle)
            await self.db.execute(stmt)
            await self.db.commit()
            return vehicle
        except Exception as e:
            print(e)
            return None
    
    async def get_all_vehicles(self) -> List[Vehicle]:
        try:
            stmt = select(Vehicle)
            result = await self.db.execute(stmt)
            vehicles = result.scalars().all()
            return vehicles
        except Exception as e:
            print(e)
            return None
    
    async def update_vehicle(self, vehicle_id: int, vehicle: Dict) -> Vehicle:
        try:
            stmt = update(Vehicle).where(Vehicle.id == vehicle_id).values(**vehicle)
            await self.db.execute(stmt)
            await self.db.commit()
            return vehicle
        except Exception as e:
            print(e)
            return None
    
    async def delete_vehicle(self, vehicle_id: int):
        try:
            stmt = delete(Vehicle).where(Vehicle.id == vehicle_id)
            await self.db.execute(stmt)
            await self.db.commit()
            return True
        except Exception as e:
            print(e)
            return None
    
    async def get_vehicle_by_id(self, vehicle_id: int) -> Vehicle:
        try:
            stmt = select(Vehicle).where(Vehicle.id == vehicle_id)
            result = await self.db.execute(stmt)
            vehicle = result.scalars().first()
            return vehicle
        except Exception as e:
            print(e)
            return None