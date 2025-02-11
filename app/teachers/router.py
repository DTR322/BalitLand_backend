from fastapi import APIRouter, Depends, Path, HTTPException

from app.auth.users.dependencies import get_current_admin_user
from app.teachers.dao import TeacherDAO
from app.teachers.rb import RBTeacherBase, RBTeacherFilter, RBTeacherRegister
from app.teachers.schemas import STeacherChange, STeacher

router = APIRouter(prefix='/teachers', tags=['Работа с преподавателями'])


@router.get("/", summary="Получить всех учителей по фильтру")
async def get_all_teachers(request_body: RBTeacherBase = Depends()) -> list[STeacher]:
    return await TeacherDAO.find_all(**request_body.to_dict())


@router.get("/get_by/", summary="Получить одного учителя по фильтру")
async def get_teacher_by_filter(request_body: RBTeacherFilter = Depends()) -> STeacher | dict:
    return await TeacherDAO.find_one_or_none(**request_body.to_dict())


@router.post("/add/", summary="добавить нового учителя")
async def add_teacher(teacher: RBTeacherRegister = Depends(get_current_admin_user)) -> STeacherChange | dict:
    check = await TeacherDAO.add(**teacher.to_dict())
    if check:
        return {"message": "Новый учитель добавлен успешно", "teacher": teacher}
    else:
        return {"message": "При добавлении учителя произошла ошибка"}


@router.put("/update_teacher/", summary="обновить данные учителя")
async def update_teacher(teacher: RBTeacherFilter = Depends(get_current_admin_user)) -> STeacherChange | dict:
    update_fields = {}

    if teacher.first_name:
        update_fields['first_name'] = teacher.first_name
    if teacher.last_name:
        update_fields['last_name'] = teacher.last_name

    if not update_fields:
        return {"message": "Нет данных для обновления."}

    check = await TeacherDAO.update(
        filter_by={'id': teacher.teacher_id},
        **update_fields
    )
    if check:
        return {"message": "Описание учителя успешно обновлено!", "teacher": teacher}
    else:
        return {"message": "Ошибка при обновлении описания учителя!"}


@router.delete("/dell/{teacher_id}", summary="удалить учителя")
async def delete_teacher(
    teacher_id: int = Path(..., title="ID учителя", description="Введите ID учителя для удаления", example=1, gt=0),
    admin_user: dict = Depends(get_current_admin_user)
) -> dict:

    if admin_user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Доступ запрещен. Только администратор может удалять учителей.")

    check = await TeacherDAO.delete_by_id(data_id=teacher_id)
    if check:
        return {"message": f"Учитель с ID {teacher_id} удален!"}
    else:
        return {"message": "Ошибка при удалении учителя!"}
