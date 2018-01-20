"""
Check08b
Yurii Vasiuk
Custom exception class
Exceptions raised and caught in different functions
"""
class NegativeNumberError(Exception):
    def __init__(self, message):
        super().__init__(message)

def get_inverse(n):
    num = int(n)
    if num < 0:
        negative_number_error = NegativeNumberError("Error: The value cannot be negative")
        raise negative_number_error
    else:
        return 1/num

def main():
    number = input("Enter a number: ")
    try:
        inverse_number = get_inverse(number)
        print("The result is: {}".format(inverse_number))
    except ValueError:
        print("Error: The value must be a number")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except NegativeNumberError as nne:
        print(nne)

if __name__ == '__main__':
    main()
