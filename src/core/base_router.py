from fastapi import APIRouter
from users.router import router as users_router

router = APIRouter()

router.include_router(
    users_router,
    prefix="/users",
    tags=["Users"]
)
