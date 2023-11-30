from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from db_config.session import get_async_session
from model.data.user import User
from model.data.task import Task
from repository.task import TaskRepo
from model.request.task import TaskCreate, TaskUpdate
from auth.auth import current_user, current_superuser

router = APIRouter()


@router.get('/get_all_tasks')
async def get_all_tasks(db: AsyncSession = Depends(get_async_session)):
    repo = TaskRepo(db)
    tasks = await repo.get_all_tasks()
    if tasks is None:
        return JSONResponse(status_code=404, content={"message": "Tasks not found"})
    return tasks

@router.post('/create_task')
async def create_task(task: TaskCreate, current_user: User = Depends(current_superuser), db: AsyncSession = Depends(get_async_session)):
    repo = TaskRepo(db)
    content = task.model_dump()
    task = await repo.insert_task(content)
    if task is None:
        return JSONResponse(status_code=404, content={"message": "Task not created"})
    return task

@router.delete('/delete_task/{task_id}')
async def delete_task(task_id: int, current_user: User = Depends(current_superuser), db: AsyncSession = Depends(get_async_session)):
    repo = TaskRepo(db)
    task = await repo.delete_task(task_id)
    if task is None:
        return JSONResponse(status_code=404, content={"message": "Task not deleted"})
    return task

@router.put('/update_task/{task_id}')
async def update_task(task_id: int, task: TaskUpdate, current_user: User = Depends(current_superuser), db: AsyncSession = Depends(get_async_session)):
    repo = TaskRepo(db)
    task = await repo.update_task(task_id, task.model_dump())
    if task is None:
        return JSONResponse(status_code=404, content={"message": "Task not updated"})
    return task