import uuid

from item import Item


class Order:
    def __init__(self, table_no):
        self.id = uuid.uuid4()
        self.table_no = table_no
        self.order_items = {}  # Item -> quantity
        self.amount = 0

    def add_item(self, item: Item, quantity):
        self.order_items[item] = quantity

    def remove_item(self, item: Item):
        if item in self.order_items:
            del self.order_items[item]
        else:
            print(f"Item {item.get_item_name()} not found in order.")

    def update_item_quantity(self, item: Item, new_quantity):
        self.order_items[item] = new_quantity

    def calculate_amount(self):
        self.amount = 0
        for item, quantity in self.order_items.items():
            self.amount += item.get_item_price() * quantity
        return self.amount
