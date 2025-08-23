from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CashStrategy(PaymentStrategy):

    def pay(self, amount):
        print(f'{amount} has been paid by cash')


class CardStrategy(PaymentStrategy):

    def pay(self, amount):
        print(f'{amount} has been paid by card')


class Payment:
    def __init__(self, strategy):
        self.strategy = strategy

    def make_payment(self, amount):
        self.strategy.pay(amount)

    def set_strategy(self, strategy):
        self.strategy = strategy


