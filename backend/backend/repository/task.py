from typing import Dict, Any, List
from sqlalchemy.ext.asyncio import AsyncSession
from model.data.task import Task
from sqlalchemy import update, delete, select, insert

class TaskRepo:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def insert_task(self, task: Dict) -> Task:
        try:
            stmt = insert(Task).values(**task)
            await self.db.execute(stmt)
            await self.db.commit()
            return task
        except Exception as e:
            print(e)
            return None
    
    async def get_all_tasks(self) -> List[Task]:
        try:
            stmt = select(Task)
            result = await self.db.execute(stmt)
            tasks = result.scalars().all()
            return tasks
        except Exception as e:
            print(e)
            return None
    
    async def update_task(self, task_id: int, task: Dict) -> Task:
        try:
            stmt = update(Task).where(Task.id == task_id).values(**task)
            await self.db.execute(stmt)
            await self.db.commit()
            return task
        except Exception as e:
            print(e)
            return None
    
    async def delete_task(self, task_id: int):
        try:
            stmt = delete(Task).where(Task.id == task_id)
            await self.db.execute(stmt)
            await self.db.commit()
            return True
        except Exception as e:
            print(e)
            return None
    
    async def get_task_by_id(self, task_id: int) -> Task:
        try:
            stmt = select(Task).where(Task.id == task_id)
            result = await self.db.execute(stmt)
            task = result.scalars().first()
            return task
        except Exception as e:
            print(e)
            return None
        
    async def get_task_by_driver_id(self, driver_id: int) -> Task:
        try:
            stmt = select(Task).where(Task.driver_id == driver_id)
            result = await self.db.execute(stmt)
            task = result.scalars().all()
            return task
        except Exception as e:
            print(e)
            return None