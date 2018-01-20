'''
team06
Inheritance
- is a - , - has a - approaches
'''

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def prompt_for_point(self):
        self.y = input("Input y: ")
        self.x = input("Input x: ")

    def display(self):
        print("Center:")
        print("({},{})".format(self.x, self.y))

class Circle_is(Point):
    def __init__(self):
        super().__init__()
        self.radius = 0

    def prompt_for_circle(self):
        self.prompt_for_point()
        self.radius = input("Input radius: ")

    def display(self):
        super().display()
        print("Radius: {}".format(self.radius))

class Circle_has():
    def __init__(self):
        self.point = Point()
        self.radius = 0

    def prompt(self):
        self.point.prompt_for_point()
        self.radius = input("Input radius: ")

    def display(self):
        print("Center:")
        self.point.display()
        print("Radius: {}".format(self.radius))


def main():
    # is a
    circle1 = Circle_is()

    circle1.prompt_for_circle()
    circle1.display()

    # has a
    circle2 = Circle_has()

    circle2.prompt()
    circle2.display()

if __name__ == '__main__':
    main()