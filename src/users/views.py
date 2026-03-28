from sqlalchemy.orm import Session,joinedload
from users.models import Student

def get_all_students(db:Session):
    data = {
        "user_data": db.query(Student).options(joinedload(Student.classroom)).all()
    }
    return data
