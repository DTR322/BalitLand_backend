from pydantic import Field, BaseModel, ConfigDict, EmailStr


class STeacher(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    teacher_id: int
    login: str = Field(..., min_length=3, max_length=32,
                       description="Логин должен быть в диапазоне от 3 до 32 символов")
    password: str = Field(..., min_length=3, max_length=32,
                          description="Пароль должен быть в диапазоне от 3 до 16 символов")
    first_name: str = Field(..., min_length=1, max_length=50, description="Имя учителя, от 1 до 50 символов")
    last_name: str = Field(..., min_length=1, max_length=50, description="Фамилия учителя, от 1 до 50 символов")
    email: EmailStr = Field(..., description="Электронная почта")


class STeacherChange(BaseModel):

    login: str = Field(..., min_length=3, max_length=32,
                       description="Логин должен быть в диапазоне от 3 до 32 символов")
    password: str = Field(..., min_length=3, max_length=32,
                          description="Пароль должен быть в диапазоне от 3 до 16 символов")
    first_name: str = Field(..., min_length=1, max_length=50, description="Имя учителя, от 1 до 50 символов")
    last_name: str = Field(..., min_length=1, max_length=50, description="Фамилия учителя, от 1 до 50 символов")
    email: EmailStr = Field(..., description="Электронная почта")

