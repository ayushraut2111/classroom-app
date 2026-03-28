from pydantic import BaseModel,computed_field
import uuid
from datetime import datetime


class ClassroomSchema(BaseModel):
    id: uuid.UUID
    slug: str
    name: str
    room_number: int
    class_teacher : str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class StudentSchema(BaseModel):
    id : uuid.UUID
    slug :str
    name : str
    phone: str
    age: int | None
    slug: str
    classroom: ClassroomSchema | None 
    created_at : datetime
    updated_at : datetime

    @computed_field
    @property
    def student_code(self) -> str:
        return f"{self.name}-{self.phone}".upper().replace(" ", "-")

    class Config:
        from_attributes = True

class GetStudentSchema(BaseModel):
    user_data: list[StudentSchema]
    total: int
    message: str
