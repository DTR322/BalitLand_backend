class RBUser:
    def __init__(self, user_id: int | None = None,
                 email: str | None = None,
                 password: str | None = None,
                 phone_number: str | None = None,
                 first_name: str | None = None,
                 last_name: str | None = None,

                 ):
        self.id = user_id
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self) -> dict:
        data = {'id': self.id, 'email': self.email, 'password': self.password,
                'phone_number': self.phone_number, 'first_name': self.first_name, 'last_name': self.last_name}
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data
