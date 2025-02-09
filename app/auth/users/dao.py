from app.dao.base import BaseDAO
from app.auth.users.models import User


class UsersDAO(BaseDAO):
    model = User
