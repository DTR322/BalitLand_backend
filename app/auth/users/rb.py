from fastapi import Form


class RBUser:
    def __int__(self, email: str | None = None,
                password: str | None = None,
                phone_number: str | None = None,
                first_name: str | None = None,
                last_name: str | None = None):

        self.email = Form(email)
        self.password = Form(password)
        self.phone_number = Form(phone_number)
        self.first_name = Form(first_name)
        self.last_name = Form(last_name)

    def to_dict(self):
        data = {'email': self.email, 'password': self.password, 'phone_number': self.phone_number,
                'first_name': self.first_name, 'last_name': self.last_name}

        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data
