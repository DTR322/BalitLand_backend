from app.dao.base import BaseDAO
from app.teachers.models import Teacher


class TeacherDAO(BaseDAO):
    model = Teacher

