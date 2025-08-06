from tomato import Tomato
from models.user import User
from models.payment_strategy import UPIPaymentStragey

def main():
    # Initialize the system
    system = Tomato()

    # Create a user
    user = User(user_id=1, name="Hritik", address="MG Road")

    # Search for restaurants
    nearby_restaurants = system.search_resturant("MG Road")
    print("\n📍 Nearby Restaurants:")
    for i, res in enumerate(nearby_restaurants, start=1):
        print(f"{i}. {res.name.title()}")

    # Select a restaurant
    selected_restaurant = nearby_restaurants[0]
    system.select_resturant(user, selected_restaurant)

    # Show menu
    print(f"\n🍽️ Menu at {selected_restaurant.name.title()}:")
    for item in selected_restaurant.get_items():
        print(f"- {item.id}: {item.name.title()} ₹{item.price}")

    # Add items to cart
    system.add_to_cart(user, item_id=1)
    system.add_to_cart(user, item_id=2)

    # Checkout
    payment_strategy = UPIPaymentStragey(upi_id="hritik@upi")
    order = system.checkoutnow(user, order_type="DILEVERY", strategy=payment_strategy)

    # Pay
    system.payment_now(user, order)

    # Show all orders
    system.ord_manager.list_orders()

if __name__ == "__main__":
    main()
