class RBStudent:
    def __init__(self, student_id: int | None = None,
                 parent_first_name: str | None = None,
                 parent_last_name: str | None = None):
        self.id = student_id
        self.parent_first_name = parent_first_name
        self.parent_last_name = parent_last_name

    def to_dict(self) -> dict:
        data = {'id': self.id, 'parent_first_name': self.parent_first_name, 'parent_last_name': self.parent_last_name}
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data
