def calc_tax(price):
    x = 10
    return price * 0.065

def calc_tip(price):
    return price * 0.2

def calc_meal_price(base_price):
    x = 20
    tax = calc_tax(base_price)
    tip = calc_tip(base_price + tax)

    total = base_price + tax + tip
    return total


def main():
    base = float(input("What is the price: "))
    total = calc_meal_price(base)

    print("Your total bill will be: {}".format(total))


if __name__ == "__main__":
    main()