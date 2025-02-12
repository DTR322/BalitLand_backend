from sqlalchemy import ForeignKey, text, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.database import Base, str_uniq, int_pk, str_null_true


class Student(Base):
    id: Mapped[int_pk]
    login: Mapped[str]
    password: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]
    klass: Mapped[int]
    school: Mapped[str]
    parent_first_name: Mapped[str]
    parent_last_name: Mapped[str]
    phone_number: Mapped[str_uniq]

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"login={self.login!r},"
                f"password={self.password!r}),"
                f"first_name={self.first_name!r},"
                f"last_name={self.last_name!r}),"
                f"klass={self.klass!r},"
                f"school={self.school!r}),"
                f"parent_first_name={self.parent_first_name!r}),"
                f"parent_last_name={self.parent_last_name!r},"
                f"phone_number={self.phone_number!r})"
                )

    def __repr__(self):
        return str(self)
