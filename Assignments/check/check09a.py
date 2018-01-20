"""
Check08a
Yurii Vasiuk
Exceptions
"""
def main():
    """
    Example of a simple exception
    :return: 
    """
    is_good_input = False

    while is_good_input == False:
        try:
            num = int(input("Enter a number: "))
            num *= 2
            print("The result is: {}".format(num))
            is_good_input = True
        except ValueError:
            print("The value entered is not valid")


if __name__ == '__main__':
    main()
