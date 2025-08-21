from reservationStatus import ReservationStatus


class Table:
    def __init__(self, table_no, capacity):
        self.table_no = table_no
        self.capacity = capacity
        self.is_available = True
        self.reservations = []

    def get_table_no(self):
        return self.table_no

    def get_capacity(self):
        return self.capacity

    #need to complete this method
    def is_table_available(self, date, start_time, end_time):
        if not self.is_available:
            for reservation in self.reservations:
                if reservation.status in [ReservationStatus.HELD, ReservationStatus.CONFIRMED] and reservation.date == date:
                    if start_time < reservation.end_time and end_time > reservation.start_time:
                        return False
        return True

    def add_reservation(self, reservation):
        self.reservations.append(reservation)

