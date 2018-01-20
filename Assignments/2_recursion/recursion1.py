def fact(n):
    if n == 0:
        return 1
    else:
        temp = n * fact(n-1)
        print("{} - {}".format(n, temp))
        return temp

def count_down(n):
    if n == 0:
        print(n)
        return n
    else:
        print("{}".format(n))
        count_down(n - 1)

        return n

def fibonacci(n):
    if n == 0:
        print("0 - 1")
        return 1
    if n == 1:
        print("1 - 1")
        return 1
    else:
        fib = fibonacci(n - 1) + fibonacci(n - 2)
        print("{} - {}".format(n, fib))
        return fib

def main():
    n = 10

    print("Factorial of {}".format(n))
    fact(n)
    print()

    print("Count down of {}".format(n))
    count_down(n)
    print()

    print("Fibonacci of {}".format(n))
    fibonacci(n)
    print()

if __name__ == '__main__':
    main()

