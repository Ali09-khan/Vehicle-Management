from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from db_config.session import get_async_session
from model.data.user import User
from model.data.role import Role
from repository.role import RoleRepo
from auth.auth import current_user, current_superuser

router = APIRouter()

@router.get('/get_all_roles')
async def get_all_roles(db: AsyncSession = Depends(get_async_session)):
    repo = RoleRepo(db)
    roles = await repo.get_all_roles()
    if roles is None:
        return JSONResponse(status_code=404, content={"message": "Roles not found"})
    return roles

@router.post('/create_role')
async def create_role(name: str, db: AsyncSession = Depends(get_async_session)):
    repo = RoleRepo(db)
    role = await repo.insert_role({'name': name})
    if role is None:
        return JSONResponse(status_code=404, content={"message": "Role not created"})
    return role