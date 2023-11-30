from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from db_config.session import get_async_session
from model.request.fueling_record import FuelingRecordCreate, FuelingRecordUpdate
from model.data.user import User
from model.data.fueling_record import FuelingRecord
from repository.fueling_record import FuelingRecordRepo
from auth.auth import require_role, current_superuser

router = APIRouter()

@router.get('/get_all_fueling_records')
async def get_all_fueling_records(user:User = Depends(require_role(4)), db: AsyncSession = Depends(get_async_session)):
    repo = FuelingRecordRepo(db)
    fueling_records = await repo.get_all_fueling_records()
    if fueling_records is None:
        return JSONResponse(status_code=404, content={"message": "Fueling records not found"})
    return fueling_records

@router.post('/create_fueling_record')
async def create_fueling_record(fueling_record: FuelingRecordCreate, user:User = Depends(require_role(4)), db: AsyncSession = Depends(get_async_session)):
    repo = FuelingRecordRepo(db)
    fueling_record = await repo.insert_fueling_record(fueling_record.model_dump())
    if fueling_record is None:
        return JSONResponse(status_code=404, content={"message": "Fueling record not created"})
    return fueling_record

@router.delete('/delete_fueling_record/{fueling_record_id}')
async def delete_fueling_record(fueling_record_id: int, user:User = Depends(require_role(4)), db: AsyncSession = Depends(get_async_session)):
    repo = FuelingRecordRepo(db)
    fueling_record = await repo.delete_fueling_record(fueling_record_id)
    if fueling_record is None:
        return JSONResponse(status_code=404, content={"message": "Fueling record not deleted"})
    return fueling_record

@router.put('/update_fueling_record/{fueling_record_id}')
async def update_fueling_record(fueling_record_id: int, fueling_record: FuelingRecordUpdate, user:User = Depends(require_role(4)), db: AsyncSession = Depends(get_async_session)):
    repo = FuelingRecordRepo(db)
    fueling_record = await repo.update_fueling_record(fueling_record_id, fueling_record.model_dump())
    if fueling_record is None:
        return JSONResponse(status_code=404, content={"message": "Fueling record not updated"})
    return fueling_record

@router.get('/get_fueling_record_by_id/{fueling_record_id}')
async def get_fueling_record_by_id(fueling_record_id: int, user:User = Depends(require_role(4)), db: AsyncSession = Depends(get_async_session)):
    repo = FuelingRecordRepo(db)
    fueling_record = await repo.get_fueling_record_by_id(fueling_record_id)
    if fueling_record is None:
        return JSONResponse(status_code=404, content={"message": "Fueling record not found"})
    return fueling_record