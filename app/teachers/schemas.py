from pydantic import Field, BaseModel, ConfigDict


class STeacher(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    login: str = Field(..., min_length=3, max_length=32,
                       description="Логин должен быть в диапазоне от 3 до 32 символов")
    password: str = Field(..., min_length=3, max_length=32,
                          description="Пароль должен быть в диапазоне от 3 до 16 символов")
    first_name: str = Field(..., min_length=1, max_length=50, description="Имя ученика, от 1 до 50 символов")
    last_name: str = Field(..., min_length=1, max_length=50, description="Фамилия ученика, от 1 до 50 символов")


class STeacherAdd(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    login: str = Field(..., min_length=3, max_length=32,
                       description="Логин должен быть в диапазоне от 3 до 32 символов")
    password: str = Field(..., min_length=3, max_length=32,
                          description="Пароль должен быть в диапазоне от 3 до 16 символов")
    first_name: str = Field(..., min_length=1, max_length=50, description="Имя ученика, от 1 до 50 символов")
    last_name: str = Field(..., min_length=1, max_length=50, description="Фамилия ученика, от 1 до 50 символов")
