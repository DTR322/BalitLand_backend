from enum import Enum
from pydantic import BaseModel, EmailStr, Field, field_validator, ValidationError
from datetime import date, datetime
from typing import Optional
import re


class student(BaseModel):
    # Информация об ученике
    student_login: str = Field(defualt=..., min_length=3, max_length=32, description="Логин ученика")
    # Что сделать с паролем? Какие у него должны быть стандарты?
    student_password: str = Field(defualt=..., min_length=3, max_length=16, description="Пароль ученика")
    first_name: str = Field(defualt=..., min_length=3, max_length=50, description="Имя")
    last_name: str = Field(defualt=..., min_length=3, max_length=50, description="Фамилия")
    # Класс, год обучения.
    course: int = Field(default=..., ge=1, le=11, description="Год обучения")
    # Информация о ком-то из родителей
    parent_first_name: str = Field(defualt=..., min_length=3, max_length=50, description="Имя родителя")
    parent_last_name: str = Field(defualt=..., min_length=3, max_length=50, description="Фамилия родителя")
    parent_number: str = Field(default=..., description="Номер телефона родителя")

    @field_validator("parents_number")
    @classmethod
    def validate_phone_number(cls, values: str) -> str:
        if not re.match(r'^\+\d{1,15}$', values):
            raise ValueError('Номер телефона должен начинаться с "+" и содержать от 1 до 15 цифр')
        return values
