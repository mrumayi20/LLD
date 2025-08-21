import uuid


class Item:
    def __init__(self, name, price):
        self.id = uuid.uuid4()
        self.item_name = name
        self.price = price

    def get_item_price(self):
        return self.price

    def get_item_name(self):
        return self.item_name