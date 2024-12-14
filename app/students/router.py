from fastapi import APIRouter
from app.students.dao import StudentDAO


router = APIRouter(prefix='/students', tags=['Работа с учениками'])


@router.get("/", summary="Получить всех учеников")
async def get_all_students():
    return await StudentDAO.find_all_students()