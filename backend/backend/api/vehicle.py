from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from db_config.session import get_async_session
from model.data.vehicle import Vehicle
from repository.vehicle import VehicleRepo
from model.request.vehicle import VehicleCreate, VehicleUpdate
from auth.auth import current_superuser
from sqlalchemy import select

router = APIRouter()

@router.get('/get_all_vehicles', dependencies=[Depends(current_superuser)])
async def get_all_vehicles(db: AsyncSession = Depends(get_async_session)):
    repo = VehicleRepo(db)
    vehicles = await repo.get_all_vehicles()
    if vehicles is None:
        return JSONResponse(status_code=404, content={"message": "Vehicles not found"})
    return vehicles

@router.post('/create_vehicle', dependencies=[Depends(current_superuser)])
async def create_vehicle(vehicle: VehicleCreate, db: AsyncSession = Depends(get_async_session)):
    repo = VehicleRepo(db)
    vehicle = await repo.insert_vehicle(vehicle.model_dump())
    if vehicle is None:
        return JSONResponse(status_code=404, content={"message": "Vehicle not created"})
    return vehicle

@router.delete('/delete_vehicle/{vehicle_id}', dependencies=[Depends(current_superuser)])
async def delete_vehicle(vehicle_id: int, db: AsyncSession = Depends(get_async_session)):
    repo = VehicleRepo(db)
    vehicle = await repo.delete_vehicle(vehicle_id)
    if vehicle is None:
        return JSONResponse(status_code=404, content={"message": "Vehicle not deleted"})
    return vehicle

@router.put('/update_vehicle/{vehicle_id}', dependencies=[Depends(current_superuser)])
async def update_vehicle(vehicle_id: int, vehicle: VehicleUpdate, db: AsyncSession = Depends(get_async_session)):
    repo = VehicleRepo(db)
    vehicle = await repo.update_vehicle(vehicle_id, vehicle.model_dump())
    if vehicle is None:
        return JSONResponse(status_code=404, content={"message": "Vehicle not updated"})
    return vehicle

@router.get('/get_vehicle_by_id/{vehicle_id}', dependencies=[Depends(current_superuser)])
async def get_vehicle_by_id(vehicle_id: int, db: AsyncSession = Depends(get_async_session)):
    repo = VehicleRepo(db)
    vehicle = await repo.get_vehicle_by_id(vehicle_id)
    if vehicle is None:
        return JSONResponse(status_code=404, content={"message": "Vehicle not found"})
    return vehicle