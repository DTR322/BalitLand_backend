from sqlalchemy.future import select
from app.database import async_session_maker
from app.students.models import Student


class BaseDAO:
    @classmethod
    async def find_all_students(cls):
        async with async_session_maker() as session:
            query = select(Student)
            students = await session.execute(query)
            return students.scalars().all()