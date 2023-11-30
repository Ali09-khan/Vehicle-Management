from typing import Dict, Any, List
from sqlalchemy.ext.asyncio import AsyncSession
from model.data.role import Role
from sqlalchemy import update, delete, select, insert

class RoleRepo:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def insert_role(self, role: Dict) -> Role:
        try:
            stmt = insert(Role).values(**role)
            await self.db.execute(stmt)
            await self.db.commit()
            return role
        except Exception as e:
            print(e)
            return None
    
    async def get_all_roles(self) -> List[Role]:
        try:
            stmt = select(Role)
            result = await self.db.execute(stmt)
            roles = result.scalars().all()
            return roles
        except Exception as e:
            print(e)
            return None