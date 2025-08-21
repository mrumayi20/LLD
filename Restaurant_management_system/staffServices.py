from staffRole import StaffRole
from menu import Menu

class StaffServices:
    def __init__(self, order_service, reservation_service):
        self.order_service = order_service
        self.reservation_service = reservation_service
        self.staffs = {}

    def take_order(self, staff, table_number, ordered_items):
        if staff.get_role() != StaffRole.WAITER:
            raise PermissionError(f"{staff.get_name()} is not allowed to take orders.")
        print(f"{staff.get_name()} is taking an order.")
        return self.order_service.create_order(table_number, ordered_items)

    def serve_food(self, staff):
        if staff.get_role() != StaffRole.WAITER:
            raise PermissionError(f"{staff.get_name()} is not allowed to serve food.")
        print(f"{staff.get_name()} is serving food.")
        # You can mark order as served here if you track status

    def handle_reservation(self, staff, table, name, date, start_time, end_tme, no_of_people):
        if staff.get_role() != StaffRole.MANAGER:
            raise PermissionError(f"{staff.get_name()} is not allowed to handle reservations.")
        print(f"{staff.get_name()} is handling reservation.")
        return self.reservation_service.make_reservation(table, name, date, start_time, end_tme, no_of_people)


    def get_menu(self):
        print('Restaurant Menu')
        menu = Menu()
        menu.get_menu()

