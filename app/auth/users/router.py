from fastapi import APIRouter, HTTPException, status, Response, Depends
from app.auth.auth import get_password_hash, authenticate_user, create_access_token, get_current_user
from app.auth.users.dao import UsersDAO
from app.auth.users.dependencies import get_current_admin_user
from app.auth.users.models import User
from app.auth.users.schemas import SUserChange, SUserAuth
from app.auth.users.rb import RBUserChange, RBUserBase

router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post("/register/", summary="создать аккаунт")
async def register_user(user_data: RBUserChange = Depends()) -> SUserChange | dict:
    user = await UsersDAO.find_one_or_none(email=user_data.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Пользователь уже существует'
        )
    user_dict = user_data.to_dict()
    user_dict['password'] = get_password_hash(user_data.password)
    await UsersDAO.add(**user_dict)
    return {'message': 'Вы успешно зарегистрированы!'}


@router.post("/login/", summary="войти в аккаунт")
async def auth_user(response: Response, user_data: RBUserBase = Depends()) -> SUserAuth | dict:
    '''
    Response здесь представляет объект Response, который используется для управления HTTP-ответом, отправляемым клиенту.
    Он позволяет установить заголовки ответа, установить куки и так далее.
    '''
    check = await authenticate_user(login=user_data.login, password=user_data.password)
    if check is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Неверная почта или пароль')
    access_token = create_access_token({"sub": str(check.id)})
    response.set_cookie(key="users_access_token", value=access_token, httponly=True)
    return {'access_token': access_token, 'refresh_token': None}


@router.get("/me/", summary="узнать информация обо мне")
async def get_me(user_data: User = Depends(get_current_user)):
    return user_data


@router.post("/logout/", summary="выйти из аккаунта")
async def logout_user(response: Response):
    response.delete_cookie(key="users_access_token")
    return {'message': 'Пользователь успешно вышел из системы'}


@router.get("/all_users/", summary="все аккаунты")
async def get_all_users(user_data: User = Depends(get_current_admin_user)):
    return await UsersDAO.find_all()
