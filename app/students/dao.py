from sqlalchemy import insert
from sqlalchemy.exc import SQLAlchemyError

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.students.models import Student


class StudentDAO(BaseDAO):
    model = Student

    @classmethod
    async def add_student(cls, student_data: dict):
        async with async_session_maker() as session:
            async with session.begin():
                # Вставка нового студента
                stmt = insert(cls.model).values(**student_data).returning(cls.model.id,)
                result = await session.execute(stmt)
                new_student_id, major_id = result.fetchone()

                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e

                return new_student_id
