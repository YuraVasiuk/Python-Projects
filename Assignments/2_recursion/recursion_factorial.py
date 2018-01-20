
def calc_factorial(num):
    """
    Returns the factorial of the given number: n!
    :param num: The num
    :return: The resulting factorial
    """

    # Base Case
    if num == 0:
        # This is the base case. We know the answer with out calculating it
        return 1

    # Regular case
    # We need to calculate this one... do it based on a simpler version
    value = num * calc_factorial(num - 1)

    print("Returning {}...".format(value))
    return value

def main():
    num = int(input("Enter number: "))
    result = calc_factorial(num)
    print("The factorial is: {}".format(result))


if __name__ == "__main__":
    main()