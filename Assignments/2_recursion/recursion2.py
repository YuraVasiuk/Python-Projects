def countdown(num):
    print(num)

    if num == 0:
        print("Blast off!")
        return
    else:
        print("Calling the function again, this time with: {}".format(num - 1))
        countdown(num - 1)
        print("Back in function: {}... returning".format(num))
        return

def main():
    countdown(3)


if __name__ == "__main__":
    main()