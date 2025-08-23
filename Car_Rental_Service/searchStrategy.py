from abc import ABC, abstractmethod


class SearchStrategy(ABC):
    @abstractmethod
    def search(self, cars, criteria):
        pass


class searchByPrice(SearchStrategy):

    def search(self, cars, price):
        res = []
        for car in cars:
            if car.get_price_per_day() <= price:
                res.append(car)
        return res


class searchByCapacity(SearchStrategy):

    def search(self, cars, capacity):
        res = []
        for car in cars:
            if car.get_capacity() >= capacity:
                res.append(car)
        return res


class SearchContext:
    def __init__(self, strategy: SearchStrategy):
        self.strategy = strategy

    def search(self, cars, criteria):
        return self.strategy.search(cars, criteria)
