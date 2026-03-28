from fastapi import APIRouter

router=APIRouter()

# here always include router apis just below it
user_router=APIRouter()
@user_router.get("/")
def get_u():
    return {"m": "sd"}




router.include_router(
    user_router,
    prefix="/user",
    tags=["User"]
)