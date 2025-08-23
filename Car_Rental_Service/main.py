from datetime import date, timedelta

from car import Car
from customer import Customer
from carRentalService import CarRentalService
from payment import CashStrategy, CardStrategy
from searchStrategy import searchByPrice, searchByCapacity, SearchContext


def print_cars(title, cars):
    print(f"\n--- {title} ---")
    if not cars:
        print("No cars found.")
        return
    for c in cars:
        print(f"{c.get_model()} ({c.year}) - {c.get_capacity()} seats - ${c.get_price_per_day()} per day")


def main():
    service = CarRentalService.get_instance()

    # Create sample cars
    car1 = Car("DL-111", "Toyota Corolla", 2020, 50, 5)
    car2 = Car("DL-222", "Honda Civic", 2021, 55, 5)
    car3 = Car("DL-333", "Ford Expedition", 2022, 90, 7)

    # Add cars
    service.add_car(car1)
    service.add_car(car2)
    service.add_car(car3)

    # Create customers
    customer1 = Customer("DL-ABC-123", "Alice", "alice@example.com")
    customer2 = Customer("DL-XYZ-456", "Bob", "bob@example.com")

    # Add customers
    service.add_customer(customer1)
    service.add_customer(customer2)

    # Search cars by price
    price_search = SearchContext(searchByPrice())
    cheap_cars = price_search.search(service.cars, 60)
    print_cars("Cars with price <= $60", cheap_cars)

    # Rent a car for Alice
    start_date = date.today()
    end_date = start_date + timedelta(days=3)
    print(f"\nRenting {car1.get_model()} for Alice from {start_date} to {end_date}")
    try:
        booking = service.rent(car1, customer1, start_date, end_date, CardStrategy())
        print(f"Booking confirmed. Amount paid: ${booking.amount}")
    except Exception as e:
        print("Booking failed:", e)

    # Try overlapping booking for Bob
    print(f"\nTrying overlapping booking on {car1.get_model()} for Bob (should fail)")
    try:
        service.rent(car1, customer2, start_date + timedelta(days=1), end_date + timedelta(days=2), CashStrategy())
        print("Overlapping booking succeeded (unexpected)")
    except Exception as e:
        print("Expected failure:", e)

    # Cancel Alice's booking
    print(f"\nCancelling Alice's booking...")
    if booking:
        result = service.crs.cancel_booking(booking)
        print("Cancelled:", result)
    else: 
        print('Alice didnot book')

    # Try again after cancellation
    print(f"\nRetrying booking for Bob (should now succeed)...")
    try:
        new_booking = service.rent(car1, customer2, start_date + timedelta(days=1), end_date + timedelta(days=2), CashStrategy())
        print(f"Booking confirmed. Amount paid: ${new_booking.amount}")
    except Exception as e:
        print("Booking failed:", e)


if __name__ == "__main__":
    main()
