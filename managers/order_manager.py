class OrderManager:
    _instance = None

    def __init__(self):
        self.orders = []

    @staticmethod
    def get_instance():
        if not OrderManager._instance:
            OrderManager._instance = OrderManager()
        return OrderManager._instance

    def add_order(self, order):
        self.orders.append(order)

    def list_orders(self):
        print("\n--- All Orders ---")
        for order in self.orders:
            print(f"{order.get_type()} order for {order.user.usr_name.title()} | Total: ₹{order.total} | At: {order.time}")
