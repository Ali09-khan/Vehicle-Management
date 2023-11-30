from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from db_config.session import get_async_session
from model.request.maintenance_record import MaintenanceRecordCreate, MaintenanceRecordUpdate
from model.data.user import User
from model.data.maintenance_record import MaintenanceRecord
from repository.maintenance_record import MaintenanceRecordRepo
from auth.auth import require_role, current_superuser

router = APIRouter()

@router.get('/get_all_maintenance_records')
async def get_all_maintenance_records(user: User = Depends(require_role(3)),db: AsyncSession = Depends(get_async_session)):
    repo = MaintenanceRecordRepo(db)
    maintenance_records = await repo.get_all_maintenance_records()
    if maintenance_records is None:
        return JSONResponse(status_code=404, content={"message": "Maintenance Records not found"})
    return maintenance_records

@router.post('/create_maintenance_record')
async def create_maintenance_record(maintenance_record: MaintenanceRecordCreate, user: User = Depends(require_role(3)), db: AsyncSession = Depends(get_async_session)):
    repo = MaintenanceRecordRepo(db)
    content = maintenance_record.model_dump()
    content["status"] = "in_progress"
    maintenance_record = await repo.insert_maintenance_record(content)
    if maintenance_record is None:
        return JSONResponse(status_code=404, content={"message": "Maintenance Record not created"})
    return maintenance_record

@router.delete('/delete_maintenance_record/{maintenance_record_id}')
async def delete_maintenance_record(maintenance_record_id: int, user: User = Depends(require_role(3)), db: AsyncSession = Depends(get_async_session)):
    repo = MaintenanceRecordRepo(db)
    maintenance_record = await repo.delete_maintenance_record(maintenance_record_id)
    if maintenance_record is None:
        return JSONResponse(status_code=404, content={"message": "Maintenance Record not deleted"})
    return maintenance_record

@router.put('/update_maintenance_record/{maintenance_record_id}')
async def update_maintenance_record(maintenance_record_id: int, maintenance_record: MaintenanceRecordUpdate, user: User = Depends(require_role(3)), db: AsyncSession = Depends(get_async_session)):
    repo = MaintenanceRecordRepo(db)
    maintenance_record = await repo.update_maintenance_record(maintenance_record_id, maintenance_record.model_dump())
    if maintenance_record is None:
        return JSONResponse(status_code=404, content={"message": "Maintenance Record not updated"})
    return maintenance_record

@router.get('/get_maintenance_record/{maintenance_record_id}')
async def get_maintenance_record(maintenance_record_id: int, user: User = Depends(require_role(3)), db: AsyncSession = Depends(get_async_session)):
    repo = MaintenanceRecordRepo(db)
    maintenance_record = await repo.get_maintenance_record_by_id(maintenance_record_id)
    if maintenance_record is None:
        return JSONResponse(status_code=404, content={"message": "Maintenance Record not found"})
    return maintenance_record

@router.put('/finish_maintenance_record/{maintenance_record_id}')
async def end_maintenance_record(maintenance_record_id: int, user: User = Depends(require_role(3)), db: AsyncSession = Depends(get_async_session)):
    repo = MaintenanceRecordRepo(db)
    maintenance_record = await repo.update_maintenance_record(maintenance_record_id, {"status": "ended"})
    if maintenance_record is None:
        return JSONResponse(status_code=404, content={"message": "Maintenance Record not ended"})
    return maintenance_record