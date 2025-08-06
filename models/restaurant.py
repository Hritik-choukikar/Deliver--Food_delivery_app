class Resturant:
    next_id = 1

    def __init__(self, name, address):
        self.res_id = Resturant.next_id
        Resturant.next_id += 1
        self.name = name.lower()
        self.res_address = address.lower()
        self.menu_items = []

    def add_item(self, item):
        self.menu_items.append(item)

    def get_items(self):
        return self.menu_items
