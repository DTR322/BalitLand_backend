from fastapi import APIRouter

from app.teachers.dao import TeacherDAO
from app.teachers.schemas import STeacher

router = APIRouter(prefix='/teachers', tags=['Работа с преподавателями'])


@router.get("/", summary="Получить всех учителей", response_model=list[STeacher])
async def get_all_teachers():
    return await TeacherDAO.find_all()
