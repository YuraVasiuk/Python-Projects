"""
File: order.py
Author: Yurii Vasiuk

This file defines the class Order which will be instantiated and used in main 
!!! Interesting in this class is that it operates products of the class Product,
but it only learns the data type in main, so the Product needs not to be imported to here
"""


class Order:
    def __init__(self):
        self.id = ""
        self.products = []

    # Adds the provided product to the list
    def add_product(self, product):
        self.products.append(product)

    # Sums the price of each product and returns it
    def get_subtotal(self):
        subtotal = 0.0
        for product in self.products:
            subtotal += product.get_total_price()

        return subtotal

    # Returns 6.5% times the subtotal
    def get_tax(self):
        tax = self.get_subtotal() * 0.065

        return tax

    # Returns the subtotal plus the tax
    def get_total(self):
        total = self.get_subtotal() + self.get_tax()

        return total

    # Displays a receipt
    def display_receipt(self):
        # I have to add these formatting to two decimal for the right display
        subtotal = '{0:.2f}'.format(self.get_subtotal())
        tax = '{0:.2f}'.format(self.get_tax())
        total = '{0:.2f}'.format(self.get_total())

        print("Order: {}".format(self.id))
        for product in self.products:
            product.display()
        print("Subtotal: ${}".format(subtotal))
        print("Tax: ${}".format(tax))
        print("Total: ${}".format(total))
