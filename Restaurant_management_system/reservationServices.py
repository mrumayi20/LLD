from table import Table
from reservation import Reservation


class ReservationServices:
    def __init__(self):
        self.reservations = {}

    def make_reservation(self, table: Table, name, date, start_time, end_time, no_of_people):
        reservation = Reservation(table.table_no, name, date, start_time, end_time, no_of_people)
        reservation.confirm_reservation()

        table.add_reservation(reservation)

        self.reservations[reservation.id] = reservation

        return reservation

    def cancel_reservation(self, reservation: Reservation):
        reservation.cancel_reservation()

    #can update/modify a reservation
    def update_reservation(self, reservation: Reservation):
        pass

    def search_reservation_by_name(self, cust_name):
        return [r for r in self.reservations.values() if r.cust_name == cust_name]


