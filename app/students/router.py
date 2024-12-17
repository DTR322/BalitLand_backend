from fastapi import APIRouter
from app.students.dao import StudentDAO
from app.students.schemas import SStudent, SStudentAdd, SStudentUpdate

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


@router.put("/update_description/")
async def update_student_description(student: SStudentUpdate) -> dict:
    update_fields = {}

    if student.student_surname:
        update_fields['password'] = student.password
    if student.parent_name:
        update_fields['phone_number'] = student.phone_number
    if student.parent_surname:
        update_fields['parent_first_name'] = student.parent_first_name
    if student.parent_contact:
        update_fields['parent_last_name'] = student.parent_last_name
    if student.student_description:
        update_fields['klass'] = student.klass

    if not update_fields:
        return {"message": "Нет данных для обновления."}

    check = await StudentDAO.update(
        filter_by={'login': student.login},
        **update_fields
    )
    if check:
        return {"message": "Описание ученика успешно обновлено!", "student": student}
    else:
        return {"message": "Ошибка при обновлении описания ученика!"}


@router.delete("/dell/{student_id}")
async def dell_student_by_id(student_id: int) -> dict:
    check = await StudentDAO.delete_student_by_id(student_id=student_id)
    if check:
        return {"message": f"Студент с ID {student_id} удален!"}
    else:
        return {"message": "Ошибка при удалении студента!"}
