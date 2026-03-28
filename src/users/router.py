from fastapi import APIRouter, Depends
from users.schemas import GetStudentSchema
from core.database import get_db
from sqlalchemy.orm import Session

from users.views import get_all_students

router=APIRouter()

# here always include router apis just below it
user_router = APIRouter()


@user_router.get("/", response_model=GetStudentSchema)
def get_all_students_api(db: Session = Depends(get_db)):
    data = {
        "user_data": get_all_students(db)
    }
    return data


router.include_router(
    user_router,
    prefix="/user",
    tags=["User"]
)