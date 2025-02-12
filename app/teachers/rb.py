from fastapi import Form

class RBTeacherBase:
    def __init__(self,
                 first_name: str | None = Form(None),
                 last_name: str | None = Form(None)):
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self) -> dict:
        data = {'first_name': self.first_name, 'last_name': self.last_name}
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data


class RBTeacherRegister:
    def __init__(self,
                 login: str | None = Form(None),
                 password: str | None = Form(None),
                 email: str | None = Form(None),
                 first_name: str | None = Form(None),
                 last_name: str | None = Form(None),):

        super().__init__(login, password, email)
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({'first_name': self.first_name, 'last_name': self.last_name})
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data


class RBTeacherFilter(RBTeacherBase):

    def __init__(self,
                 teacher_id: str | None = Form(None),
                 first_name: str | None = Form(None),
                 last_name: str | None = Form(None)
                 ):

        super().__init__(first_name, last_name)

        self.teacher_id = teacher_id

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({'teacher_id': self.teacher_id})
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data
