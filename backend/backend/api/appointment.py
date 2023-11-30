from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from db_config.session import get_async_session
from model.request.appointment import AppointmentCreate, AppointmentUpdate
from model.data.user import User
from model.data.appointment import Appointment
from repository.appointment import AppointmentRepo
from repository.appointment import AppointmentRepo
from auth.auth import require_role, current_superuser

router = APIRouter()

@router.post("/create_appointment")
async def create_appointment(appointment: AppointmentCreate, user: User = Depends(require_role(3)),db: AsyncSession = Depends(get_async_session)):
    repo = AppointmentRepo(db)
    appointment = await repo.insert_appointment(appointment.model_dump())
    if appointment is None:
        return JSONResponse(status_code=404, content={"message": "Appointment not created"})
    return appointment

@router.get("/get_all_appointments")
async def get_all_appointments(user: User = Depends(require_role(3)), db: AsyncSession = Depends(get_async_session)):
    repo = AppointmentRepo(db)
    appointments = await repo.get_all_appointments()
    if appointments is None:
        return JSONResponse(status_code=404, content={"message": "Appointments not found"})
    return appointments

@router.put("/update_appointment/{appointment_id}")
async def update_appointment(appointment_id: int, appointment: AppointmentUpdate, user: User = Depends(require_role(3)), db: AsyncSession = Depends(get_async_session)):
    repo = AppointmentRepo(db)
    appointment = await repo.update_appointment(appointment_id, appointment.model_dump())
    if appointment is None:
        return JSONResponse(status_code=404, content={"message": "Appointment not updated"})
    return appointment

@router.delete("/delete_appointment/{appointment_id}")
async def delete_appointment(appointment_id: int, user: User = Depends(require_role(3)), db: AsyncSession = Depends(get_async_session)):
    repo = AppointmentRepo(db)
    appointment = await repo.delete_appointment(appointment_id)
    if appointment is None:
        return JSONResponse(status_code=404, content={"message": "Appointment not deleted"})
    return appointment

@router.get("/get_appointment_by_id/{appointment_id}")
async def get_appointment_by_id(appointment_id: int, user: User = Depends(require_role(3)), db: AsyncSession = Depends(get_async_session)):
    repo = AppointmentRepo(db)
    appointment = await repo.get_appointment_by_id(appointment_id)
    if appointment is None:
        return JSONResponse(status_code=404, content={"message": "Appointment not found"})
    return appointment