from item import Item


class Menu:
    def __init__(self):
        self.menu_item = {}

    def add_item_in_menu(self, item: Item):
        self.menu_item[item.get_item_name()] = item

    def remove_item_from_menu(self, item):
        item_name = item.get_item_name()
        del self.menu_item[item_name]

    def update_meu_item_price(self, item, new_price):
        item_name = item.get_item_name()
        self.menu_item[item_name] = new_price

    def get_menu(self):
        return self.menu_item
