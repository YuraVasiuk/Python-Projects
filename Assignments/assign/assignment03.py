'''
Assignment03
'''

# the class to use in the Robot
class Point:
    def __init__(self):
        self.x = 10
        self.y = 10
    #END OF POINT


# the main class
class Robot:
    def __init__(self):
        self.coordinates = Point()
        self.fuel = 100

    def display(self):
        print("({}, {}) - Fuel: {}".format(self.coordinates.x, self.coordinates.y, self.fuel))

    def move(self, direction):
        if self.fuel < 5:
            print("Insufficient fuel to perform action")
        elif direction == "left":
            self.coordinates.x -= 1
            self.fuel -= 5
        elif direction == "right":
            self.coordinates.x += 1
            self.fuel -= 5
        elif direction == "up":
            self.coordinates.y -= 1
            self.fuel -= 5
        elif direction == "down":
            self.coordinates.y += 1
            self.fuel -= 5

    def fire(self, command):
        if self.fuel < 15:
            print("Insufficient fuel to perform action")
        else:
            print("Pew! Pew!")
            self.fuel -= 15
    #END OF ROBOT


def main():
    # make the object
    robot = Robot()

    # interact with the user using the object
    command = " "
    while command != "quit":
        command = input("Enter command: ")
        if command == "left" or command == "right" or command == "up" or command == "down":
            robot.move(command)
        if command == "fire":
            robot.fire(command)
        if command == "status":
            robot.display()

    print("Goodbye.")
    # END OF MAIN

if __name__ == "__main__":
    main()