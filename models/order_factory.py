from abc import ABC, abstractmethod
from models.order import PickUpOrder, DileveryOrder

class OrderFactory(ABC):
    @abstractmethod
    def create_order(self, user, cart, restaurant, order_type, strategy):
        pass

class ScheduledOrderFactory(OrderFactory):
    def __init__(self, time):
        self.time = time

    def create_order(self, user, cart, restaurant, order_type, strategy):
        if order_type == "DILEVERY":
            order = DileveryOrder()
            order.user_address = user.usr_address
        else:
            order = PickUpOrder()
            order.restaurant_address = restaurant.res_address

        order.user = user
        order.restaurant = restaurant
        order.order_type = order.get_val()
        order.strategy = strategy
        order.total = cart.get_total()
        order.items = cart.get_items()
        order.time = self.time

        return order

class NowOrderFactory(OrderFactory):
    def create_order(self, user, cart, restaurant, order_type, strategy):
        if order_type == "DILEVERY":
            order = DileveryOrder()
            order.user_address = user.usr_address
        else:
            order = PickUpOrder()
            order.restaurant_address = restaurant.res_address

        order.user = user
        order.restaurant = restaurant
        order.order_type = order.get_val()
        order.strategy = strategy
        order.total = cart.get_total()
        order.items = cart.get_items()
        order.time = "current_time"

        return order
