from sqlalchemy.orm import Session,joinedload
from users.models import Student

def get_all_students(db:Session):
    return db.query(Student).options(joinedload(Student.classroom)).all()
