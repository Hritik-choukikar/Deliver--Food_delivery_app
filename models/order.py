from abc import ABC, abstractmethod

class Order(ABC):
    next_id = 1

    def __init__(self):
        self.order_id = Order.next_id
        Order.next_id += 1
        self.user = None
        self.restaurant = None
        self.total = 0.0
        self.items = []
        self.time = ""
        self.strategy = None
        self.order_type = None

    def pay_now(self):
        if self.strategy:
            self.strategy.pay(self.total)
            return True
        else:
            print("Please select a payment strategy first.")
            return False

    @abstractmethod
    def get_val(self):
        pass

    def get_type(self):
        return self.order_type

class PickUpOrder(Order):
    def __init__(self):
        super().__init__()
        self.restaurant_address = None

    def get_val(self):
        return "PICKUP"

class DileveryOrder(Order):
    def __init__(self):
        super().__init__()
        self.user_address = None

    def get_val(self):
        return "DILEVERY"
