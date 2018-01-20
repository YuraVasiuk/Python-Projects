"""
Team09
Yurii Vasiuk
Exceptions handling
"""
class BalanceError(Exception):
    """
    Check the balance error
    """
    def __init__(self, message=""):
        super().__init__(message)

class OutOfChecksError(Exception):
    """
    Check the check errors
    """
    def __init__(self, message=""):
        super().__init__(message)

class CheckingAccount():
    """
    The blueprint fo creating an account
    """
    def __init__(self, starting_balance = 0.0, num_checks = 0):
        if starting_balance < 0:
            negative_balance = BalanceError("Cancelled! The amount cannot be negative!")
            raise negative_balance
        self.balance = starting_balance
        self.check_count = num_checks

    def deposit(self, amount):
        self.balance += amount

    def write_check(self, amount):
        if amount > self.balance:
            inadequate_balance = BalanceError("Cancelled! The amount of check is bigger than the balance!")
            raise inadequate_balance
        if self.check_count < 1:
            no_checks = OutOfChecksError("Cancelled! There is no checks available!")
            raise no_checks
        self.balance -= amount
        self.check_count -= 1

    def display(self):
        print("The current balance: {}".format(round(self.balance, 2)))
        print("The number of checks: {}".format(self.check_count))

    def apply_for_credit(self, amount):
        pass


def display_menu():
    """
    Displays the available commands.
    """
    print()
    print("Commands:")
    print("  quit - Quit")
    print("  new - Create new account")
    print("  display - Display account information")
    print("  deposit - Deposit money")
    print("  check - Write a check")


def main():
    """
    Used to test the CheckingAccount class.
    """
    acc = None
    command = ""

    while command != "quit":
        display_menu()
        command = input("Enter a command: ")

        if command == "new":
            try:
                balance = float(input("Starting balance: "))
                num_checks = int(input("Numbers of checks: "))

                acc = CheckingAccount(balance, num_checks)
            except BalanceError as ba:
                print(ba)
        elif command == "display":
            acc.display()
        elif command == "deposit":
            try:
                amount = float(input("Amount: "))
                acc.deposit(amount)
            except BalanceError as ba:
                print(ba)
        elif command == "check":
            try:
                amount = float(input("Amount: "))
                acc.write_check(amount)
            except BalanceError as ba:
                print(ba)
            except OutOfChecksError as oc:
                print(oc)
                by_checks = input("Would you like to by checks?(y/n): ")
                if by_checks == "y":
                    acc.balance -= 5
                    acc.check_count += 25
        elif command == "credit":
            amount = float(input("Amount: "))
            acc.apply_for_credit(amount)


if __name__ == "__main__":
    main()