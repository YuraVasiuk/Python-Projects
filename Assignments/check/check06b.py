'''
Check 06b
Inheritance
Yurii Vasiuk
'''

# parent class
class Phone():
    def __init__(self):
        self.area_code = 0
        self.prefix = 0
        self.suffix = 0
        self.smart = False

    def prompt_number(self):
        if self.smart == False:
            print("Phone:")
        self.area_code = input("Area Code: ")
        self.prefix = input("Prefix: ")
        self.suffix = input("Suffix: ")

    def display(self):
        print("Phone info:")
        print("({}){}-{}".format(self.area_code, self.prefix, self.suffix))

# chils class
class SmartPhone(Phone):
    def __init__(self):
        self.email = ""
        self.smart = True

    def prompt(self):
        if self.smart == True:
            print("Smart phone:")
        self.prompt_number()
        self.email = input("Email: ")

    def display(self):
        super().display()
        print("{}".format(self.email))


def main():
    # use parent class
    phone = Phone()
    phone.prompt_number()
    print()
    phone.display()
    print()

    # use child class
    smart_phone = SmartPhone()
    smart_phone.prompt()
    print()
    smart_phone.display()

if __name__ == "__main__":
    main()

