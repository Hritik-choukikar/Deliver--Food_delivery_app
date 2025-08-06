from managers.restaurant_manager import ResturantManager
from managers.order_manager import OrderManager
from models.menu_item import MenuItems
from models.order_factory import NowOrderFactory, ScheduledOrderFactory

class Tomato:
    def __init__(self):
        self.res_manager = ResturantManager.get_instance()
        self.ord_manager = OrderManager.get_instance()
        self.initialize()

    def initialize(self):
        from models.restaurant import Resturant

        res1 = self._create_restaurant("Pizza Palace", "MG Road", [
            MenuItems(1, "Margherita Pizza", 250),
            MenuItems(2, "Farmhouse Pizza", 300)
        ])
        res2 = self._create_restaurant("Burger Hub", "MG Road", [
            MenuItems(3, "Veg Burger", 120),
            MenuItems(4, "Cheese Burger", 150)
        ])
        res3 = self._create_restaurant("Sushi Corner", "Park Street", [
            MenuItems(5, "California Roll", 350),
            MenuItems(6, "Spicy Tuna Roll", 400)
        ])

        self.res_manager.add_resturant(res1)
        self.res_manager.add_resturant(res2)
        self.res_manager.add_resturant(res3)

        print("🍅 Tomato system initialized with sample restaurants and menus.")

    def _create_restaurant(self, name, address, items):
        from models.restaurant import Resturant
        res = Resturant(name, address)
        res.menu_items = items
        return res

    def search_resturant(self, loc):
        return self.res_manager.search_by_location(loc)

    def select_resturant(self, user, restaurant):
        user.cart.restaurant = restaurant

    def add_to_cart(self, user, item_id):
        for item in user.cart.restaurant.get_items():
            if item.id == item_id:
                print(f"Item with ID {item_id} added to cart.")
                user.cart.add_item(item)

    def checkoutnow(self, user, order_type, strategy):
        return self.checkout(user, order_type, strategy, NowOrderFactory())

    def checkoutscheduled(self, user, order_type, strategy, time):
        return self.checkout(user, order_type, strategy, ScheduledOrderFactory(time))

    def checkout(self, user, order_type, strategy, factory):
        if user.cart.is_empty():
            print("Please select a restaurant first.")
            return None
        order = factory.create_order(user, user.cart, user.cart.restaurant, order_type, strategy)
        self.ord_manager.add_order(order)
        return order

    def payment_now(self, user, order):
        if order.pay_now():
            user.cart.clear()
