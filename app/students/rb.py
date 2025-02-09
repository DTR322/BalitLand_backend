from fastapi import Form


class RBStudentBase:
    def __init__(self,
                 first_name: str | None = Form(None),
                 last_name: str | None = Form(None),
                 parent_first_name: str | None = Form(None),
                 parent_last_name: str | None = Form(None),
                 klass: str | None = Form(None),
                 phone_number: str | None = Form(None),
                 ):
        self.parent_first_name = parent_first_name
        self.parent_last_name = parent_last_name
        self.klass = klass
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self) -> dict:
        data = {'first_name': self.first_name, 'last_name': self.last_name,
                'parent_first_name': self.parent_first_name, 'parent_last_name': self.parent_last_name,
                'klass': self.klass, 'phone_number': self.phone_number}
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data


class RBStudentAdd(RBStudentBase):

    def __init__(self,
                 first_name: str | None = Form(None),
                 last_name: str | None = Form(None),
                 parent_first_name: str | None = Form(None),
                 parent_last_name: str | None = Form(None),
                 klass: str | None = Form(None),
                 phone_number: str | None = Form(None),
                 login: str | None = Form(None),
                 password: str | None = Form(None)
                 ):
        super().__init__(first_name, last_name, parent_first_name, parent_last_name, klass, phone_number)

        self.login = login
        self.password = password

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({'login': self.login, 'password': self.password})
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data


class RBStudentFilter(RBStudentBase):

    def __init__(self,
                 student_id: int | None = Form(None),
                 first_name: str | None = Form(None),
                 last_name: str | None = Form(None),
                 parent_first_name: str | None = Form(None),
                 parent_last_name: str | None = Form(None),
                 klass: str | None = Form(None),
                 phone_number: str | None = Form(None)
                 ):
        super().__init__(first_name, last_name, parent_first_name, parent_last_name, klass, phone_number)
        self.student_id = student_id

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({'student_id': self.student_id})
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data