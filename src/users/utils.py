from sqlalchemy.orm import Session,joinedload
from users.models import Student
from users.schemas import StudentCreateSchema

def get_all_students(db:Session):
    return db.query(Student).options(joinedload(Student.classroom)).all()


def create_student(data: StudentCreateSchema, db: Session):

    # first check whethe student exist or not by phone number

    instance = db.query(Student).filter(Student.phone == data.phone).first()

    if instance:
        return instance

    student = Student(
        name=data.name,
        age=data.age,
        phone=data.phone,
        classroom_id=data.classroom_id
    )

    student.save(db)

    return student
