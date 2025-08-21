from staff import Staff
from table import Table


class RestaurantManagementSystem:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.initialized = False
        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls()

    def __init__(self):
        if self.initialized is False:
            self.staff = []
            self.tables = []
            self.initialized = True

    def add_tables(self, table_no, capacity):
        table = Table(table_no, capacity)
        self.tables.append(table)

    def add_staff(self, name, role):
        person = Staff(name, role)
        self.staff.append(person)

    def find_available_table(self, capacity, date, start_time, end_time):
        for table in self.tables:
            if table.capacity >= capacity and table.is_table_available(date, start_time, end_time):
                return table

        print('No table is available, we are fully booked')
        return None

