from datetime import datetime, date
from typing import Optional
import re
from pydantic import BaseModel, Field, EmailStr, validator, ConfigDict


class SStudent(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    login: str = Field(..., min_length=3, max_length=32,
                       description="Логин должен быть в диапазоне от 3 до 32 символов")
    password: str = Field(..., min_length=3, max_length=16,
                          description="Пароль должен быть в диапазоне от 3 до 16 символов")
    first_name: str = Field(..., min_length=1, max_length=50, description="Имя ученика, от 1 до 50 символов")
    last_name: str = Field(..., min_length=1, max_length=50, description="Фамилия ученика, от 1 до 50 символов")
    klass: int = Field(..., ge=1, le=11, description="Класс должен быть в диапазоне от 1 до 11")
    school: str
    parent_first_name: str = Field(..., min_length=1, max_length=50, description="Имя родителя, от 1 до 50 символов")
    parent_last_name: str = Field(..., min_length=1, max_length=50, description="Фамилия родителя, от 1 до 50 символов")
    phone_number: str = Field(..., description="Номер телефона в международном формате, начинающийся с '+'")


class SStudentAdd(BaseModel):
    login: str = Field(..., min_length=3, max_length=32,
                       description="Логин должен быть в диапазоне от 3 до 32 символов")
    password: str = Field(..., min_length=3, max_length=16,
                          description="Пароль должен быть в диапазоне от 3 до 16 символов")
    first_name: str = Field(..., min_length=1, max_length=50, description="Имя ученика, от 1 до 50 символов")
    last_name: str = Field(..., min_length=1, max_length=50, description="Фамилия ученика, от 1 до 50 символов")
    klass: int = Field(..., ge=1, le=11, description="Класс должен быть в диапазоне от 1 до 11")
    school: str
    parent_first_name: str = Field(..., min_length=1, max_length=50, description="Имя родителя, от 1 до 50 символов")
    parent_last_name: str = Field(..., min_length=1, max_length=50, description="Фамилия родителя, от 1 до 50 символов")
    phone_number: str = Field(..., description="Номер телефона в международном формате, начинающийся с '+'")


class SStudentUpdate(BaseModel):
    login: str = Field(..., min_length=3, max_length=32,
                       description="Логин должен быть в диапазоне от 3 до 32 символов")
    password: str = Field(..., min_length=3, max_length=16,
                          description="Пароль должен быть в диапазоне от 3 до 16 символов")
    first_name: str = Field(..., min_length=1, max_length=50, description="Имя ученика, от 1 до 50 символов")
    last_name: str = Field(..., min_length=1, max_length=50, description="Фамилия ученика, от 1 до 50 символов")
    klass: int = Field(..., ge=1, le=11, description="Класс должен быть в диапазоне от 1 до 11")
    school: str
    parent_first_name: str = Field(..., min_length=1, max_length=50, description="Имя родителя, от 1 до 50 символов")
    parent_last_name: str = Field(..., min_length=1, max_length=50, description="Фамилия родителя, от 1 до 50 символов")
    phone_number: str = Field(..., description="Номер телефона в международном формате, начинающийся с '+'")
