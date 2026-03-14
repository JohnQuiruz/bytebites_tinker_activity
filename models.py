'''
Four classes in the ByteBites design:
1. Customer - represents a user with a name and purchase history (list of Transactions)
2. FoodItem - represents a menu item with a name, price, category, and popularity rating
3. FoodItemCollection - a container for FoodItems that supports filtering by category
4. Transaction - represents a single order containing one or more FoodItems, with a computed total
'''

from enum import Enum


class Category(Enum):
    BURGERS = "Burgers"
    DRINKS = "Drinks"
    DESSERTS = "Desserts"
    SIDES = "Sides"


class FoodItem:
    def __init__(self, name, price, category):
        self._name = name
        self._price = price
        self._category = category
        self._popularity_rating = 0.0

    def get_name(self):
        pass

    def get_price(self):
        pass

    def get_category(self):
        pass

    def get_popularity_rating(self):
        pass

    def set_popularity_rating(self, rating):
        pass


class FoodItemCollection:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        pass

    def get_items(self):
        pass

    def filter_by_category(self, category):
        pass


class Transaction:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.items = []

    def get_customer_id(self):
        pass

    def add_item(self, item):
        pass

    def get_items(self):
        pass

    def compute_total(self):
        pass


class Customer:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.purchase_history = []

    def get_id(self):
        pass

    def get_name(self):
        pass

    def set_name(self, name):
        pass

    def get_purchase_history(self):
        pass

    def add_transaction(self, transaction):
        pass
