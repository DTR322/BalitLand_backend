from sqlalchemy import ForeignKey, text, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.auth.users.models import User
from app.database import Base, str_uniq, int_pk, str_null_true
from datetime import date


class Student(Base):
    id: Mapped[int_pk]
    first_name: Mapped[str]
    last_name: Mapped[str]
    klass: Mapped[int]
    school: Mapped[str]
    parent_first_name: Mapped[str]
    parent_last_name: Mapped[str]
    phone_number: Mapped[str_uniq]

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped[User] = relationship("User", back_populates="students")

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"first_name={self.first_name!r},"
                f"last_name={self.last_name!r})")

    def __repr__(self):
        return str(self)
