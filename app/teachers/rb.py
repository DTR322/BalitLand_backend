class RBTeacher:
    def __init__(self, teacher_id: int | None = None,
                 first_name: str | None = None,
                 last_name: str | None = None):
        self.id = teacher_id
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self) -> dict:
        data = {'id': self.id, 'parent_first_name': self.first_name, 'parent_last_name': self.last_name}
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data
