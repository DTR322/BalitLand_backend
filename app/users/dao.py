from sqlalchemy import select, delete

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.users.models import User


class UsersDAO(BaseDAO):
    model = User

    @classmethod
    async def delete_user_by_id(cls, user_id: int):
        async with async_session_maker() as session:
            async with session.begin():
                query = select(cls.model).filter_by(id=user_id)
                result = await session.execute(query)
                student_to_delete = result.scalar_one_or_none()

                if not student_to_delete:
                    return None

                # Удаляем студента
                await session.execute(
                    delete(cls.model).filter_by(id=user_id)
                )

                await session.commit()
                return user_id
