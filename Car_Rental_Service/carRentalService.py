from car import Car
from customer import Customer
from payment import PaymentStrategy
from rentalService import RentalService
from searchStrategy import SearchContext


class CarRentalService:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.initialize = False

        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls()

    def __init__(self):
        if self.initialize is False:
            self.cars = []
            self.customers = []
            self.crs = RentalService()

    def add_car(self, car):
        self.cars.append(car)

    def add_customer(self, customer):
        self.customers.append(customer)

    def rent(self, car: Car, customer: Customer, start_date, end_date, paymentStrategy: PaymentStrategy):
        return self.crs.rent_car(car, customer, start_date, end_date, paymentStrategy)

    def search(self, strategy, criteria):
        searching = SearchContext(strategy)
        return searching.search(self.cars, criteria)