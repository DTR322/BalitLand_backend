from fastapi import APIRouter, HTTPException, status, Response, Depends
from app.users.auth import get_password_hash, authenticate_user, create_access_token, get_current_user
from app.users.dao import UsersDAO
from app.users.dependencies import get_current_admin_user
from app.users.models import User
from app.users.rb import RBUser
from app.users.schemas import SUserRegister, SUserAuth, SUserUpdate

router = APIRouter(prefix='/auth', tags=['Auth'])


# Регистрация
@router.post("/register/")
async def register_user(user_data: SUserRegister) -> dict:
    user = await UsersDAO.find_one_or_none(email=user_data.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Пользователь уже существует'
        )
    user_dict = user_data.dict()
    user_dict['password'] = get_password_hash(user_data.password)
    await UsersDAO.add(**user_dict)
    return {'message': 'Вы успешно зарегистрированы!'}


# Вход в систему
@router.post("/login/")
async def auth_user(response: Response, user_data: SUserAuth):
    check = await authenticate_user(email=user_data.email, password=user_data.password)
    if check is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Неверная почта или пароль')
    access_token = create_access_token({"sub": str(check.id)})
    response.set_cookie(key="users_access_token", value=access_token, httponly=True)
    return {'access_token': access_token, 'refresh_token': None}


'''
response здесь представляет объект Response, который используется для управления HTTP-ответом, отправляемым клиенту.
Он позволяет установить заголовки ответа, установить куки и так далее.
'''


# Изменить данные аккаунт
@router.put("/update_description/")
async def update_student_description(user_data: RBUser = Depends()) -> SUserUpdate | dict:
    update_fields = {}

    if user_data.email:
        update_fields['email'] = user_data.email
    if user_data.password:
        update_fields['password'] = user_data.password
    if user_data.phone_number:
        update_fields['phone_number'] = user_data.phone_number
    if user_data.first_name:
        update_fields['first_name'] = user_data.first_name
    if user_data.last_name:
        update_fields['last_name'] = user_data.last_name

    if not update_fields:
        return {"message": "Нет данных для обновления."}

    check = await UsersDAO.update(
        filter_by={'login': User.email},
        **update_fields
    )
    if check:
        return {"message": "Описание пользователя успешно обновлено!", "student": user_data}
    else:
        return {"message": "Ошибка при обновлении описания пользователя!"}


# Удаление аккаунта
@router.delete("/dell/{user_id}")
async def dell_student_by_id(user_id: int) -> dict:
    check = await UsersDAO.delete_user_by_id(user_id=user_id)
    if check:
        return {"message": f"Пользователь с ID {user_id} удален!"}
    else:
        return {"message": "Ошибка при удалении пользователя!"}


@router.post("/logout/")
async def logout_user(response: Response):
    response.delete_cookie(key="users_access_token")
    return {'message': 'Пользователь успешно вышел из системы'}


@router.get("/me/")
async def get_me(user_data: User = Depends(get_current_user)):
    return user_data


@router.get("/all_users/")
async def get_all_users(user_data: User = Depends(get_current_admin_user)):
    return await UsersDAO.find_all()
