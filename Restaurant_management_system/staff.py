import uuid
from staffRole import StaffRole


class Staff:
    def __init__(self, name, role: StaffRole):
        self.id = uuid.uuid4()
        self.name = name
        self.role = role

    def get_name(self):
        return self.name

    def get_role(self):
        return self.role


