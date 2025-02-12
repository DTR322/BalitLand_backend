from fastapi import Depends, HTTPException
from starlette import status

from app.auth.auth import get_current_user
from app.teachers.models import Teacher


async def get_current_admin_user(current_user: Teacher = Depends(get_current_user)):
    if current_user.is_admin:
        return current_user
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Недостаточно прав!')