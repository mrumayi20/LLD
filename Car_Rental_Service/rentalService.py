from threading import Lock

from booking import Booking
from bookingStatus import BookingStatus
from car import Car
from customer import Customer
from payment import Payment, PaymentStrategy


class RentalService:
    def __init__(self):
        self.bookings = {}
        self.lock = Lock()

    def rent_car(self, car: Car, customer: Customer, start_date, end_date, paymentStrategy: PaymentStrategy):
        with self.lock:
            if car.is_car_available(start_date, end_date):
                # calculate_price
                total_price = car.price_per_day * (end_date - start_date).days

                # booking generate
                booking = Booking(car, customer, start_date, end_date, total_price)

                # make payment
                payment = Payment(paymentStrategy)
                payment.make_payment(total_price)

                # Confirm booking
                booking.confirm_booking()

                # add booking to hmap
                self.bookings[booking.id] = booking
                car.bookings.append(booking)

                return booking

        raise Exception(f'{car.get_model()} is not available')

    def cancel_booking(self, booking: Booking):
        with self.lock:
            if booking.id in self.bookings:
                booking.cancel_booking()
                return True
            print('Booking not found')
        return False

    def modify_booking(self,booking_id,new_car=None,new_start_date=None,new_end_date=None,payment_strategy=None):
        with self.lock:
            booking = self.bookings.get(booking_id)
            if not booking:
                raise Exception("Booking not found")

            old_car = booking.get_car()
            start_date = new_start_date or booking.get_start_date()
            end_date = new_end_date or booking.get_end_date()
            car = new_car or old_car

            # Check availability of the new car (exclude this booking's own range)
            for other_booking in car.get_bookings().values():
                if other_booking.get_booking_id() == booking_id or other_booking.status != BookingStatus.CONFIRMED:
                    continue
                if not (end_date <= other_booking.get_start_date() or start_date >= other_booking.get_end_date()):
                    raise Exception("Selected car is not available in the new date range")

            # Update car if changed
            if new_car and new_car != old_car:
                # Remove from old car
                old_car.get_bookings().pop(booking_id, None)
                # Add to new car
                new_car.add_bookings(booking)
                booking.car = new_car

            # Update dates and recalculate amount
            # Recalculate amount
            new_days = (end_date - start_date).days + 1
            new_amount = car.get_price_per_day() * new_days

            old_amount = booking.amount
            booking.start_date = start_date
            booking.end_date = end_date
            booking.amount = new_amount

            # Handle payment difference
            if new_amount > old_amount:
                difference = new_amount - old_amount
                print(f"Additional payment of ${difference} required.")
                if payment_strategy:
                    payment = Payment(payment_strategy)
                    payment.make_payment(difference)
                else:
                    print("No payment strategy provided. Please pay manually.")
            elif new_amount < old_amount:
                print(f"Booking amount decreased by ${old_amount - new_amount}. (Refund logic not implemented)")

            print(f"Booking {booking_id} has been modified successfully.")
