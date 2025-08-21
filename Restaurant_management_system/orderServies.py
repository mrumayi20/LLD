from order import Order


class OrderServices:
    def __init__(self):
        self.orders = {}

    def create_order(self, table_no, order_items):
        order = Order(table_no)

        for item, quantity in order_items:
            order.add_item(item, quantity)

        self.orders[order.id] = order
        return order


