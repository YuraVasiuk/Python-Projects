"""
File: product.py
Author: Yurii Vasiuk

This file defines the class Product which will be instantiated and used in main 
"""


class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    # Returns the price multiplied by the quantity
    def get_total_price(self):
        total_price = self.price * self.quantity

        return total_price

    # Displays the products name, quantity, and total price
    def display(self):
        # I have to add this formatting to two decimal for the right display
        total_price = '{0:.2f}'.format(self.get_total_price())

        print("{} ({}) - ${}".format(self.name, self.quantity, total_price))