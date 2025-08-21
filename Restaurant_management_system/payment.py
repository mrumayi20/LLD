from abc import ABC, abstractmethod


class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CashStrategy(PaymentStrategy):
    def pay(self, amount):
        print(f'{amount} paid by Cash')


class CardStrategy(PaymentStrategy):
    def pay(self, amount):
        print(f'{amount} paid by card')


class Payment:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def make_payment(self, amount):
        self.strategy.pay(amount)

    def set_strategy(self, strategy):
        self.strategy = strategy
