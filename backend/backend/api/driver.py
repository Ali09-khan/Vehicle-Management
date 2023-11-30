from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from db_config.session import get_async_session
from model.request.driver import DriverCreate, DriverUpdate
from model.data.user import User
from model.data.driver import Driver
from repository.driver import DriverRepo
from repository.task import TaskRepo
from auth.auth import require_role, current_superuser

router = APIRouter()

@router.get("/me")
async def get_me(current_user: User = Depends(require_role(2)), db: AsyncSession = Depends(get_async_session)):
    repo = DriverRepo(db)
    driver = await repo.get_driver_by_id(current_user.id)
    if driver is None:
        return JSONResponse(status_code=404, content={"message": "Driver not found"})
    return driver
    
@router.post("/create_driver", dependencies=[Depends(current_superuser)])
async def create_driver(driver: DriverCreate, db: AsyncSession = Depends(get_async_session)):
    repo = DriverRepo(db)
    driver = await repo.create_driver(driver.model_dump())
    if driver is None:
        return JSONResponse(status_code=404, content={"message": "Driver not created"})
    return driver

@router.get('/get_my_tasks')
async def get_tasks(current_user: User = Depends(require_role(2)), db: AsyncSession = Depends(get_async_session)):
    repo = TaskRepo(db)
    driver_repo = DriverRepo(db)
    driver = await driver_repo.get_driver_by_id(current_user.id)
    tasks = await repo.get_task_by_driver_id(driver.id)
    if tasks is None:
        return JSONResponse(status_code=404, content={"message": "Tasks not found"})
    return tasks

@router.put('/finish_task/{task_id}')
async def end_task(task_id: int, current_user: User = Depends(require_role(2)), db: AsyncSession = Depends(get_async_session)):
    repo = TaskRepo(db)
    task = await repo.update_task(task_id, {"status": "ended"})
    if task is None:
        return JSONResponse(status_code=404, content={"message": "Task not ended"})
    return task

@router.get('/get_all_drivers', dependencies=[Depends(current_superuser)])
async def get_all_drivers(db: AsyncSession = Depends(get_async_session)):
    repo = DriverRepo(db)
    drivers = await repo.get_all_drivers()
    if drivers is None:
        return JSONResponse(status_code=404, content={"message": "Drivers not found"})
    return drivers