from models import Category, FoodItem, FoodItemCollection, Transaction, Customer

# Food items
burger = FoodItem("Spicy Burger", 9.99, Category.BURGERS)
soda = FoodItem("Large Soda", 2.99, Category.DRINKS)
fries = FoodItem("Seasoned Fries", 3.49, Category.SIDES)
brownie = FoodItem("Chocolate Brownie", 4.99, Category.DESSERTS)

# Menu
menu = FoodItemCollection()
menu.add_item(burger)
menu.add_item(soda)
menu.add_item(fries)
menu.add_item(brownie)

# Customer
customer = Customer("c001", "Alice")

# Transaction
transaction = Transaction("c001")
transaction.add_item(burger)
transaction.add_item(soda)

burger.set_popularity_rating(4.9)
print(burger.get_popularity_rating())