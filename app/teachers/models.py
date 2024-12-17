from sqlalchemy.orm import Mapped

from app.database import Base, int_pk, str_uniq


class Teacher(Base):
    id: Mapped[int_pk]
    login: Mapped[str_uniq]
    password: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"first_name={self.first_name!r},"
                f"last_name={self.last_name!r})")

    def __repr__(self):
        return str(self)

