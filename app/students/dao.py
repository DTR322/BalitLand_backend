from sqlalchemy import select
from app.students.models import Student
from app.database import async_session_maker


class StudentDAO:
    @classmethod
    async def find_all_students(cls):
        async with async_session_maker() as session:
            query = select(Student)
            students = await session.execute(query)
            return students.scalars().all()