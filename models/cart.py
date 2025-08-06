class Cart:
    def __init__(self):
        self.restaurant = None
        self.cart_items = []

    def get_total(self):
        return sum(item.price for item in self.cart_items)

    def get_items(self):
        return self.cart_items

    def add_item(self, item):
        self.cart_items.append(item)

    def clear(self):
        self.cart_items = []

    def is_empty(self):
        return not self.restaurant
