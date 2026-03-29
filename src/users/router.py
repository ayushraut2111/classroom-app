from fastapi import APIRouter, Depends, HTTPException
from classrooms.models import Classroom
from users.schemas import GetStudentSchema, StudentCreateSchema, StudentSchema
from core.database import get_db
from sqlalchemy.orm import Session
from typing import Union
from fastapi.responses import JSONResponse

from users.utils import create_student, get_all_students

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


@user_router.post("/", response_model=Union[StudentSchema, dict], status_code=200)
def add_student_api(data: StudentCreateSchema, db: Session = Depends(get_db)):

    # first check whether classroom exist or not

    classroom = db.query(Classroom).filter(
        Classroom.id == data.classroom_id).first()

    if not classroom:
        return JSONResponse(
            status_code=400,
            content={"msg": "Classroom not found"}
        )

    return create_student(data, db)

router.include_router(
    user_router,
    prefix="/user",
    tags=["User"]
)