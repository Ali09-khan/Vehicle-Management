from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from db_config.session import get_async_session
from model.data.user import User
from auth.auth import current_superuser
from sqlalchemy import select

router = APIRouter()

@router.get('/get_all_users', dependencies=[Depends(current_superuser)])
async def get_all_users(db: AsyncSession = Depends(get_async_session)):
    stmt = select(User)
    result = await db.execute(stmt)
    users = result.scalars().all()
    if users is None:
        return JSONResponse(status_code=404, content={"message": "Users not found"})
    return users