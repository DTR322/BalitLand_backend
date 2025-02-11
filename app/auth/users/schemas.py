from pydantic import BaseModel, EmailStr, Field, validator
import re


class SUserChange(BaseModel):
    user_id: int
    login: str = Field(..., min_length=5, max_length=50, description="Логин, от 5 до 50 знаков")
    password: str = Field(..., min_length=5, max_length=50, description="Пароль, от 5 до 50 знаков")
    email: EmailStr = Field(..., description="Электронная почта")


    @validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        if "@" not in value:
            raise ValueError('Email должен содержать символ "@".')
        local_part, domain_part = value.split("@", 1)
        if "." not in domain_part:
            raise ValueError('Email должен содержать символ "." после "@".')
        return value


# модель для авторизации пользователя
class SUserAuth(BaseModel):
    login: str = Field(..., min_length=5, max_length=50, description="Логин, от 5 до 50 знаков")
    password: str = Field(..., min_length=5, max_length=50, description="Пароль, от 5 до 50 знаков")