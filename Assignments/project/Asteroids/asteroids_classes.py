"""
Asteroid Classes
All the classes to be used by asteroids.py
Author Yurii Vasiuk
"""
import math
import random
import arcade
from abc import ABC
from abc import abstractmethod


# Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_REAR_THRUST_AMOUNT = 0.1
SHIP_RADIUS = 30

INITIAL_ROCK_COUNT = 5

BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2

"""
The next two classes will only be used as parts of other classes
has_a relationship
"""
class Point:
    """
    1 Point
    """
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y

class Velocity:
    """
    2 Velocity
    """
    def __init__(self, dx = 0, dy = 0):
        self.dx = dx
        self.dy = dy

class FlyingObject(ABC):
    """
    This is the basic abstract class
    it will branch out into Ship, Bullet, and Asteroid 
    """
    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        self.alive = True
        self.radius = 0.0
        self.angle = 0.0

    # these two methods are used the same way by all flying objects
    # inheritance
    def wrap(self, screen_width, screen_height):
        """
        return the leaving screen object on the other side of the screen
        :param screen_width: 
        :param screen_height: 
        :return: 
        """
        if self.center.x > screen_width + 30:
            self.center.x = 0 - 30
        if self.center.x < 0 - 30:
            self.center.x = screen_width + 30
        if self.center.y > screen_height + 30:
            self.center.y = 0 - 30
        if self.center.y < 0 - 30:
            self.center.y = screen_height + 30

    def advance(self):
        """
        Move the object with every new frame for the distance of dx and dy
        :return: 
        """
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    # abstract methods (have to be defined in every child class)
    @abstractmethod
    def draw(self):
        pass

    def hit(self):
        """
        This method is the same for all FOs
        assign alive to False and use it for removing the dead object in the "asteroids.py"
        :return: 
        """
        self.alive = False

class Ship(FlyingObject):
    """
    Properties and methods of the ship
    """
    def __init__(self):
        super().__init__()
        self.center.x = SCREEN_WIDTH / 2
        self.center.y = SCREEN_HEIGHT / 2
        self.radius = SHIP_RADIUS
        self.alive = True

    def draw(self):
        """
        draw the ship
        :return: 
        """
        img = "images/playerShip1_orange.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        alpha = 1  # For transparency, 1 means not transparent

        x = self.center.x
        y = self.center.y
        angle = self.angle

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha)

    """
    This block of methods handles moving the ship (turns, calculate the change of velocity
    for moving forward and slowing down; 
    for advancing the ship the parent class method "advance()" is called in "asteroids.py")
    """
    def turn_left(self):
        """
        # 1 (3 degrees at a time, with the wrap angle logic)
        :return: 
        """
        if self.angle >= 360:
            self.angle = 0
        self.angle += 3

    def turn_right(self):
        """
        # 2 (3 degrees at a time, with the wrap angle logic)
        :return: 
        """
        if self.angle <= 0:
            self.angle = 360
        self.angle -= 3

    def thrust(self):
        """
        # 3 recalculate the ship's velocity (acceleration)
        :return: 
        """
        # the logic for getting the right angle and recalculating the velocity
        # depends on what quarter-sphere the "self.angle" is in
        # upper left quarter-sphere
        if self.angle >= 0 and self.angle <= 90:
            thrust_angle = 90 - self.angle
            self.velocity.dx -= math.cos(math.radians(thrust_angle)) * SHIP_THRUST_AMOUNT
            self.velocity.dy += math.sin(math.radians(thrust_angle)) * SHIP_THRUST_AMOUNT

        # lower left quarter-sphere
        if self.angle > 90 and self.angle < 180:
            thrust_angle = self.angle - 90
            self.velocity.dx -= math.cos(math.radians(thrust_angle)) * SHIP_THRUST_AMOUNT
            self.velocity.dy -= math.sin(math.radians(thrust_angle)) * SHIP_THRUST_AMOUNT

        # lower right quarter-sphere
        if self.angle >= 180 and self.angle <= 270:
            thrust_angle = 270 - self.angle
            self.velocity.dx += math.cos(math.radians(thrust_angle)) * SHIP_THRUST_AMOUNT
            self.velocity.dy -= math.sin(math.radians(thrust_angle)) * SHIP_THRUST_AMOUNT

        # upper right quarter-sphere
        if self.angle > 270 and self.angle < 360:
            thrust_angle = self.angle - 270
            self.velocity.dx += math.cos(math.radians(thrust_angle)) * SHIP_THRUST_AMOUNT
            self.velocity.dy += math.sin(math.radians(thrust_angle)) * SHIP_THRUST_AMOUNT

    def rear_thrust(self):
        """
        the method is mirroring the "thrust" velocity calculations to the opposite 
        for slowing down or moving backward (uses the lower "SHIP_SLOW_DOWN" coefficient)
        :return: 
        """
        # upper left quarter-sphere
        if self.angle >= 0 and self.angle <= 90:
            thrust_angle = 90 - self.angle
            self.velocity.dx += math.cos(math.radians(thrust_angle)) * SHIP_REAR_THRUST_AMOUNT
            self.velocity.dy -= math.sin(math.radians(thrust_angle)) * SHIP_REAR_THRUST_AMOUNT

        # lower left quarter-sphere
        if self.angle > 90 and self.angle < 180:
            thrust_angle = self.angle - 90
            self.velocity.dx += math.cos(math.radians(thrust_angle)) * SHIP_REAR_THRUST_AMOUNT
            self.velocity.dy += math.sin(math.radians(thrust_angle)) * SHIP_REAR_THRUST_AMOUNT

        # lower right quarter-sphere
        if self.angle >= 180 and self.angle <= 270:
            thrust_angle = 270 - self.angle
            self.velocity.dx -= math.cos(math.radians(thrust_angle)) * SHIP_REAR_THRUST_AMOUNT
            self.velocity.dy += math.sin(math.radians(thrust_angle)) * SHIP_REAR_THRUST_AMOUNT

        # upper right quarter-sphere
        if self.angle > 270 and self.angle < 360:
            thrust_angle = self.angle - 270
            self.velocity.dx -= math.cos(math.radians(thrust_angle)) * SHIP_REAR_THRUST_AMOUNT
            self.velocity.dy -= math.sin(math.radians(thrust_angle)) * SHIP_REAR_THRUST_AMOUNT

class Bullet(FlyingObject):
    """
    Properties and methods of bullets 
    """
    def __init__(self):
        super().__init__()
        self.radius = BULLET_RADIUS
        self.lives = BULLET_LIFE

    def fire(self, ship):
        """
        1) assign the values of the point and the velocity of the ship to the fired bullet 
        2) recalculate the velocity for the fired bullet
           (add 10 pixels per frame in the direction the ship is pointed to the assigned ship velocity)
        :param ship: 
        :return: 
        """
        self.center.x = ship.center.x
        self.center.y = ship.center.y
        self.velocity.dx = ship.velocity.dx
        self.velocity.dy = ship.velocity.dy
        self.angle = ship.angle + 90

        self.velocity.dx += math.cos(math.radians(self.angle)) * BULLET_SPEED
        self.velocity.dy += math.sin(math.radians(self.angle)) * BULLET_SPEED

    def draw(self):
        """
        1) all FOs are drawn the same way
        except of the path on the first line
        2) decrease one live on every draw
        :return: 
        """
        img = "images/laserBlue01.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        alpha = 1  # For transparency, 1 means not transparent

        x = self.center.x
        y = self.center.y
        angle = self.angle

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha)

        self.lives -= 1

"""
The cluster of asteroid classes
"""
class Asteroid(FlyingObject):
    """
    This is the parent for different asteroids
    """
    def __init__(self):
        """
        Get everything from the parent class,
        ,pick random rotation angle, 
        and initiate the list of fractions for breaking the asteroid apart
        """
        super().__init__()
        random_choice = random.randint(0, 1)
        if random_choice == 0:
            self.spin = 1
        else:
            self.spin = -1
        self.fractions = list()

        def advance(self):
            """
            call the parent advance and adjust the angle if needed
            :return: 
            """
            super().advance()
            if self.angle > 360:
                self.angle = 0
            if self.angle < 0:
                self.angle = 360

        @abstractmethod
        def break_apart(self):
            """
            this method is implemented differently for different asteroids
            :param self: 
            :return: 
            """
            pass

"""
The next three classes inherit from Asteroid
and make specific adjustments for different kinds of asteroids
"""
class BigAsteroid(Asteroid):
    """
    1
    """
    def __init__(self, point, velocity):
        super().__init__()
        self.center = point
        self.velocity = velocity
        self.radius = BIG_ROCK_RADIUS

    def draw(self):
        """
        all asteroids are drawn the same way
        except of the path on the first line
        :return: 
        """
        img = "images/meteorGrey_big1.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        alpha = 1  # For transparency, 1 means not transparent

        x = self.center.x
        y = self.center.y
        angle = self.angle

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha)

    def advance(self):
        """
        call the parent advance and add
        changing the rotation angle for this kind of asteroid accordingly to the game specifications
        :return: 
        """
        super().advance()
        self.angle += (BIG_ROCK_SPIN * self.spin)

    def break_apart(self):
        """
        # 1 make two medium and one small asteroids,
        # 2 put them into the list of fractions for using int the "explode()" in "asteroids.py" 
        :return: 
        """
        # 1
        # make the first medium asteroid
        point1 = Point()
        point1.x = self.center.x
        point1.y = self.center.y
        velocity1 = Velocity()
        velocity1.dx = self.velocity.dx
        velocity1.dy = self.velocity.dy + 2
        fraction1 = MediumAsteroid(point1, velocity1)
        # make the second medium asteroid
        point2 = Point()
        point2.x = self.center.x
        point2.y = self.center.y
        velocity2 = Velocity()
        velocity2.dx = self.velocity.dx
        velocity2.dy = self.velocity.dy - 2
        fraction2 = MediumAsteroid(point2, velocity2)
        # make the small asteroid
        point3 = Point()
        point3.x = self.center.x
        point3.y = self.center.y
        velocity3 = Velocity()
        velocity3.dx = self.velocity.dx + 5
        velocity3.dy = self.velocity.dy
        fraction3 = SmallAsteroid(point3, velocity3)

        # 2
        self.fractions.append(fraction1)
        self.fractions.append(fraction2)
        self.fractions.append(fraction3)

class MediumAsteroid(Asteroid):
    """
    2
    """
    def __init__(self, point, velocity):
        super().__init__()
        self.center = point
        self.velocity = velocity
        self.radius = MEDIUM_ROCK_RADIUS

    def draw(self):
        """
        all asteroids are drawn the same way
        except of the path on the first line
        :return: 
        """
        img = "images/meteorGrey_med1.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        alpha = 1  # For transparency, 1 means not transparent

        x = self.center.x
        y = self.center.y
        angle = self.angle

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha)

    def advance(self):
        """
        call the parent advance and add
        changing the rotation angle for this kind of asteroid accordingly to the game specifications
        :return: 
        """
        super().advance()
        self.angle += (MEDIUM_ROCK_SPIN * self.spin)

    def break_apart(self):
        """
        # 1 make two small asteroids,
        # 2 put them into the list of fractions for using int the "explode()" in "asteroids.py" 
        :return: 
        """
        # 1
        # make the first small asteroid
        point1 = Point()
        point1.x = self.center.x
        point1.y = self.center.y
        velocity1 = Velocity()
        velocity1.dx = self.velocity.dx + 1.5
        velocity1.dy = self.velocity.dy + 1.5
        fraction1 = SmallAsteroid(point1, velocity1)
        # make the second medium asteroid
        point2 = Point()
        point2.x = self.center.x
        point2.y = self.center.y
        velocity2 = Velocity()
        velocity2.dx = self.velocity.dx - 1.5
        velocity2.dy = self.velocity.dy - 1.5
        fraction2 = SmallAsteroid(point2, velocity2)

        # 2
        self.fractions.append(fraction1)
        self.fractions.append(fraction2)

class SmallAsteroid(Asteroid):
    """
    3
    """
    def __init__(self, point, velocity):
        super().__init__()
        self.center = point
        self.velocity = velocity
        self.radius = SMALL_ROCK_RADIUS

    def draw(self):
        """
        all asteroids are drawn the same way
        except of the path on the first line
        :return: 
        """
        img = "images/meteorGrey_small1.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        alpha = 1  # For transparency, 1 means not transparent

        x = self.center.x
        y = self.center.y
        angle = self.angle

        arcade.draw_texture_rectangle(x, y, width, height, texture, angle, alpha)

    def advance(self):
        """
        call the parent advance and add
        changing the rotation angle for this kind of asteroid accordingly to the game specifications
        :return: 
        """
        super().advance()
        self.angle += (SMALL_ROCK_SPIN * self.spin)

    def break_apart(self):
        """
        the small asteroid does not split apart
        :return: 
        """
        pass
