from core.models import BaseModel, SlugBaseModel
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey
import uuid
from classrooms.models import Classroom


class Student(SlugBaseModel):
    __tablename__ = "students"

    name: Mapped[str] = mapped_column(unique=True)
    age: Mapped[int | None] = mapped_column(default=0, nullable=True)
    phone: Mapped[str] = mapped_column(String(20))
    classroom_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("classrooms.id")) # it tells that foreignkey must exist in classroom tables ids
    classroom: Mapped[Classroom] = relationship(back_populates="students") # it tells that in classroom there must be students, this is just a relationship this doesnt create any column in db
