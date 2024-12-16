from sqlalchemy import insert
from sqlalchemy.exc import SQLAlchemyError

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.students.models import Student


class StudentDAO(BaseDAO):
    model = Student

