from model.data.user import User
from redis import asyncio as aioredis
from fastapi.middleware.cors import CORSMiddleware


from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from auth.manager import get_user_manager
from auth.auth import auth_backend
from auth.schemas import UserCreate, UserRead, UserUpdate

from api import driver, role, users, task, vehicle, appointment, maintenance_record, fueling_record

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)



app = FastAPI()

origins = ['http://localhost:8080']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/api/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/api/auth",
    tags=["auth"],
)


app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

app.include_router(
    driver.router,
    prefix="/api/driver",
    tags=["driver"],
)
app.include_router(
    role.router,
    prefix="/api/role",
    tags=["role"],
)

app.include_router(
    users.router,
    prefix="/api/users",
    tags=["users"],
)

app.include_router(
    task.router,
    prefix="/api/task",
    tags=["task"],
)

app.include_router(
    vehicle.router,
    prefix="/api/vehicle",
    tags=["vehicle"],
)

app.include_router(
    appointment.router,
    prefix="/api/appointment",
    tags=["appointment"],
)

app.include_router(
    maintenance_record.router,
    prefix="/api/maintenance_record",
    tags=["maintenance_record"],
)

app.include_router(
    fueling_record.router,
    prefix="/api/fueling_record",
    tags=["fueling_record"],
)
