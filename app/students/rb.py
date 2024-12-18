class RBStudent:
    def __init__(self,
                 parent_first_name: str | None = None,
                 parent_last_name: str | None = None,
                 klass: str | None = None,
                 password: str | None = None,
                 login: str | None = None,
                 phone_number: str | None = None

                 ):
        self.parent_first_name = parent_first_name
        self.parent_last_name = parent_last_name
        self.klass = klass
        self.password = password
        self.login = login
        self.phone_number = phone_number

    def to_dict(self) -> dict:
        data = {'parent_first_name': self.parent_first_name, 'parent_last_name': self.parent_last_name,
                'klass': self.klass, 'password': self.password, 'login': self.login, 'phone_number': self.phone_number}
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data

