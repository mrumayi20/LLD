from bookingStatus import BookingStatus


class Car:
    def __init__(self, license_no, model, year, price_per_day, capacity):
        self.license_no = license_no
        self.model = model
        self.year = year
        self.price_per_day = price_per_day
        self.capacity = capacity
        self.bookings = []

    def get_license_no(self):
        return self.license_no

    def get_model(self):
        return self.model

    def get_price_per_day(self):
        return self.price_per_day

    def get_capacity(self):
        return self.capacity

    def add_booking(self, booking):
        self.bookings.append(booking)

    def is_car_available(self, start_date, end_date):
        for booking in self.bookings:
            if booking.status in (BookingStatus.HELD, BookingStatus.CONFIRMED):
                if (start_date < booking.end_date) and (end_date > booking.start_date):
                    return False

        return True

