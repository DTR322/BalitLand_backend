from typing import List

from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base, str_uniq, int_pk

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.students.models import Student  # Импортируем только для проверки типов


class User(Base):

    id: Mapped[int_pk]
    phone_number: Mapped[str_uniq]
    email: Mapped[str_uniq]
    login: Mapped[str_uniq]
    password: Mapped[str]
    students: Mapped[List["Student"]] = relationship("Student", back_populates="user", cascade="all, delete-orphan")

    is_user: Mapped[bool] = mapped_column(default=True, server_default=text('true'), nullable=False)
    is_student: Mapped[bool] = mapped_column(default=False, server_default=text('false'), nullable=False)
    is_teacher: Mapped[bool] = mapped_column(default=False, server_default=text('false'), nullable=False)
    is_admin: Mapped[bool] = mapped_column(default=False, server_default=text('false'), nullable=False)

    extend_existing = True

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id})"
