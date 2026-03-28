from fastapi import APIRouter, Depends
from users.schemas import GetStudentSchema
from core.database import get_db
from sqlalchemy.orm import Session

from users.utils import get_all_students

router=APIRouter()

# here always include router apis just below it
user_router = APIRouter()


@user_router.get("/", response_model=GetStudentSchema, status_code=200)
def get_all_students_api(db: Session = Depends(get_db)):
    students = get_all_students(db)
    data = {
        "user_data": students,
        "total": len(students),
        "message": "students fetched sucessfully"
    }
    return data


router.include_router(
    user_router,
    prefix="/user",
    tags=["User"]
)