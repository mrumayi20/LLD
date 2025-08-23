import uuid

from bookingStatus import BookingStatus
from car import Car
from customer import Customer


class Booking:
    def __init__(self, car: Car, customer: Customer, start_date, end_date, amount):
        self.id = uuid.uuid4()
        self.car = car
        self.customer = customer
        self.start_date = start_date
        self.end_date = end_date
        self.amount = amount
        self.status = BookingStatus.HELD

    def confirm_booking(self):
        self.status = BookingStatus.CONFIRMED

    def cancel_booking(self):
        self.status = BookingStatus.CANCELLED




