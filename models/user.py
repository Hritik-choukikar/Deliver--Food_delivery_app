from models.cart import Cart

class User:
    def __init__(self, user_id, name, address):
        self.user_id = user_id
        self.usr_name = name.lower()
        self.usr_address = address.lower()
        self.cart = Cart()
