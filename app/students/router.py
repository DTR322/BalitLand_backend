from fastapi import APIRouter, Depends, Path
from app.students.dao import StudentDAO
from app.students.rb import RBStudentBase, RBStudentFilter, RBStudentAdd
from app.students.schemas import SStudent, SStudentChange

router = APIRouter(prefix='/students', tags=['Работа с учениками'])


@router.get("/", summary="Получить всех студентов по фильтру")
async def get_all_students(request_body: RBStudentBase = Depends()) -> list[SStudent]:
    return await StudentDAO.find_all(**request_body.to_dict())


@router.post("/add/", summary="Добавить Ученика")
async def register_user(student: RBStudentAdd = Depends()) -> SStudentChange | dict:
    check = await StudentDAO.add(**student.to_dict())
    if check:
        return {"message": "Ученик успешно добавлен!", "student": student}
    else:
        return {"message": "Ошибка при добавлении ученика!"}


@router.put("/update_description/", summary="Обновить ученика")
async def update_student_description(student: RBStudentAdd = Depends()) -> SStudentChange | dict:
    update_fields = {}

    if student.password:
        update_fields['password'] = student.password
    if student.phone_number:
        update_fields['phone_number'] = student.phone_number
    if student.parent_first_name:
        update_fields['parent_first_name'] = student.parent_first_name
    if student.parent_last_name:
        update_fields['parent_last_name'] = student.parent_last_name
    if student.klass:
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


@router.delete("/dell/{student_id}", summary="Удалить ученика")
async def dell_teacher_by_id(student_id: int = Path()) -> dict:
    check = await StudentDAO.delete_by_id(data_id=student_id)
    if check:
        return {"message": f"Студент с ID {student_id} удален!"}
    else:
        return {"message": "Ошибка при удалении студента!"}
