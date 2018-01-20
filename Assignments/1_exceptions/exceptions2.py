class TooBigError(Exception):
    def __init__(self, message=""):
        super().__init__(message)

is_good_input = False

while not is_good_input:
    try:
        num = int(input("Enter num: "))

        if num > 1000:
            my_new_error = TooBigError("That is too big")
            raise my_new_error

        print("Your number is: {}".format(num))
        is_good_input = True
    except TooBigError as thing:
        print("We appreciate your love for large numbers, however this program can't handle it")
    except Exception as ex:
        print("Sorry, that is not valid.")
        print(ex)
