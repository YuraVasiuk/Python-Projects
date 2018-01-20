"""
File: customer.py
Author: Yurii Vasiuk

This file defines the class Customer which will be instantiated and used in main 
!!! Same as in the order class, orders are used but not instantiated in this class.
Different from C++ that orders[] never specifies the datatype.
"""


class Customer:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.orders = []

    # Returns the number of orders
    def get_order_counts(self):
        order_counts = 0
        for order in self.orders:
            order_counts += 1

        return order_counts

    # Returns the total price of all orders combined
    def get_total(self):
        total = 0.0
        for order in self.orders:
            total += order.get_total()

        return total

    # Adds the provided order to the list of orders
    def add_order(self, order):
        self.orders.append(order)

    # Displays a summary
    def display_summary(self):
        # I have to add these formatting to two decimal for the right display
        total = '{0:.2f}'.format(self.get_total())

        print("Summary for customer '{}':".format(self.id))
        print("Name: {}".format(self.name))
        print("Orders: {}".format(self.get_order_counts()))
        print("Total: ${}".format(total))

    # Displays all the orders' receipts
    def display_receipts(self):
        print("Detailed receipts for customer '{}':".format(self.id))
        print("Name: {}".format(self.name))
        for order in self.orders:
            print()
            order.display_receipt()


