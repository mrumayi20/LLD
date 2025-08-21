import uuid

from reservationStatus import ReservationStatus


class Reservation:
    def __init__(self, table_no, cust_name, date, start_time, end_time, no_of_people):
        self.id = uuid.uuid4()
        self.table_no = table_no
        self.cust_name = cust_name
        self.date = date
        self.status = ReservationStatus.HELD
        self.start_time = start_time
        self.end_time = end_time
        self.no_of_people = no_of_people

    def confirm_reservation(self):
        self.status = ReservationStatus.CONFIRMED

    def cancel_reservation(self):
        self.status = ReservationStatus.CANCELLED


