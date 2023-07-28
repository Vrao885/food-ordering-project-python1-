class FoodItem:
    next_food_id = 1

    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = FoodItem.next_food_id
        FoodItem.next_food_id += 1
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

    def __str__(self):
        return f"{self.name} ({self.quantity}) [INR {self.price}]"


class Restaurant:
    def __init__(self):
        self.food_items = []

    def add_food_item(self, food_item):
        self.food_items.append(food_item)

    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                return True
        return False

    def view_food_items(self):
        for food_item in self.food_items:
            print(food_item)

    def remove_food_item(self, food_id):
        self.food_items = [food_item for food_item in self.food_items if food_item.food_id != food_id]


class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password


class Order:
    def __init__(self):
        self.selected_items = []

    def select_food_items(self, food_items):
        self.selected_items = food_items

    def view_selected_items(self):
        print("Selected items:")
        for item in self.selected_items:
            print(item)

    def place_order(self):
        total_price = sum(item.price for item in self.selected_items)
        print(f"Order placed. Total amount to pay: INR {total_price}")


if __name__ == "__main__":
    restaurant = Restaurant()

    # Adding food items
    restaurant.add_food_item(FoodItem("Tandoori Chicken", "4 pieces", 240, 0, 30))
    restaurant.add_food_item(FoodItem("Vegan Burger", "1 piece", 320, 0, 20))
    restaurant.add_food_item(FoodItem("Truffle Cake", "500gm", 900, 0, 15))

    # Viewing food items
    print("List of food items:")
    restaurant.view_food_items()

    # Editing a food item
    restaurant.edit_food_item(food_id=1, name="Tandoori Chicken", quantity="8 pieces", price=400, discount=0, stock=25)

    # Removing a food item
    restaurant.remove_food_item(food_id=2)

    # Viewing updated food items
    print("\nUpdated list of food items:")
    restaurant.view_food_items()

    # User registration
    user = User("John Doe", "1234567890", "john@example.com", "123 Main St, City", "password123")

    # User place a new order
    order = Order()
    order.select_food_items([restaurant.food_items[0], restaurant.food_items[1]])
    order.view_selected_items()
    order.place_order()

    # Order history
    # Assuming we have a list of previous orders, we can display them here.
