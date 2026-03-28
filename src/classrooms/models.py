from core.models import BaseModel,SlugBaseModel
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import String
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from users.models import Student

class Classroom(SlugBaseModel):

    __tablename__ = "classrooms"

    name : Mapped[str] = mapped_column(String(255),nullable=False,unique=True) # nullable. = False is optional as in mapped we have not specifed none
    room_number : Mapped[int] = mapped_column(unique=True)
    class_teacher: Mapped[str | None] = mapped_column(String(255))
    students : Mapped[list["Student"]] = relationship(back_populates="classroom")
