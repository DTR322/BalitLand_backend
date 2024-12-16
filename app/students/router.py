from fastapi import APIRouter
from app.students.dao import StudentDAO
from app.students.schemas import SStudent, SStudentAdd

router = APIRouter(prefix='/students', tags=['Работа с учениками'])


@router.get("/", summary="Получить всех учеников", response_model=list[SStudent])
async def get_all_students():
    return await StudentDAO.find_all()


@router.post("/add/")
async def register_user(student: SStudentAdd) -> dict:
    check = await StudentDAO.add(**student.dict())
    if check:
        return {"message": "Ученик успешно добавлен!", "student": student}
    else:
        return {"message": "Ошибка при добавлении ученика!"}
