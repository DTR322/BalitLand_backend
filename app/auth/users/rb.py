from fastapi import Form


class RBUserBase:
    def __init__(self, login: str | None = Form(None),
                 password: str | None = Form(None)):
        self.login = login
        self.password = password

    def to_dict(self) -> dict:
        data = {'login': self.login, 'password': self.password}

        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data


class RBUserChange(RBUserBase):

    def __init__(self, login: str | None = Form(None),
                 password: str | None = Form(None),
                 email: str | None = Form(None)):
        super().__init__(login, password)
        self.email = email

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({'email': self.email})
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data
