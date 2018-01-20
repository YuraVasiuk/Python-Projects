
def get_name():
    name = input("Enter name")

    if name == "burton":
        raise ValueError("Sorry, we don't like you.")

    print(name)

def get_name_wrapper():
    get_name()

def main():
    try:
        get_name_wrapper()
    except:
        print("I guess something happened")


main()