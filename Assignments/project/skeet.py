"""
File: skeet.py
Original Author: Br. Burton
Designed to be completed by others
This program implements an awesome version of skeet.
"""
import arcade
import math
import random

# These are Global constants to use throughout the game
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

RIFLE_WIDTH = 100
RIFLE_HEIGHT = 20
RIFLE_COLOR = arcade.color.DARK_RED

BULLET_RADIUS = 3
BULLET_COLOR = arcade.color.BLACK_OLIVE
BULLET_SPEED = 10

TARGET_RADIUS = 20
TARGET_COLOR = arcade.color.CARROT_ORANGE
TARGET_SAFE_COLOR = arcade.color.AIR_FORCE_BLUE
TARGET_SAFE_RADIUS = 15

from abc import ABC
from abc import abstractmethod

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
    it will branch out into Bullet and Target 
    """
    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        self.alive = True

    # these two methods are used the same way by all flying objects
    # inheritance
    def is_off_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        if self.center.x > SCREEN_WIDTH or self.center.y > SCREEN_HEIGHT or self.center.y < 0:
            return True

    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    @abstractmethod
    def draw(self):
        """
        this method will be overridden in the child classes
        polymorphism
        :return: 
        """
        pass

    @abstractmethod
    def hit(self):
        """
        this method will be overridden in the child classes
        polymorphism
        :return: 
        """
        pass


class Bullet(FlyingObject):
    """
    Bullet is a flying object
    """
    def __init__(self):
        super().__init__()
        self.radius = BULLET_RADIUS

    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, BULLET_COLOR)

    def hit(self):
        self.alive = False

    # this calculates the velocity for each bullet
    # at the moment of shooting, based on the angle passed as the parameter
    # some trigonometry to spice programming :)
    def fire(self, angle):
        self.velocity.dx = math.cos(math.radians(angle)) * BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(angle)) * BULLET_SPEED


class Target(FlyingObject):
    """
    Target inherits from the FlyingObject, 
    and it is a parent class for four specific targets used in the game
    """
    def __init__(self):
        super().__init__()
        self.center.x = 0
        self.center.y = random.uniform(SCREEN_HEIGHT // 2, SCREEN_HEIGHT)
        self.velocity.dx = random.randint(1, 5)
        self.velocity.dy = random.randint(-2, 5)
        self.radius = TARGET_RADIUS


"""
The four targets inherit from the parent class
"""
class StandardTarget(Target):
    """
    1
    """
    def __init__(self):
        super().__init__()

    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, TARGET_COLOR)

    def hit(self):
        self.alive = False
        return 1

class StrongTarget(Target):
    """
    2
    """
    def __init__(self):
        """
        velocity is calculated differently for this kind of target
        lives is added
        """
        super().__init__()
        self.velocity.dx = random.randint(1, 3)
        self.velocity.dy = random.randint(-2, 3)
        self.lives = 3

    def draw(self):
        arcade.draw_circle_outline(self.center.x, self.center.y, self.radius, TARGET_COLOR)
        text_x = self.center.x - (self.radius / 2)
        text_y = self.center.y - (self.radius / 2)
        arcade.draw_text(repr(self.lives), text_x, text_y, TARGET_COLOR, font_size=20)

    # simple logic to comply with the game requirements for this kind of target
    # it is applied in the check_collisions() in Game for calculating the score
    def hit(self):
        if self.lives > 1:
            self.lives -= 1
            return 1
        else:
            self.alive = False
            return 5


class SafeTarget(Target):
    """
    3
    """
    def __init__(self):
        """
        radius is overridden for this kind of target
        """
        super().__init__()
        self.radius = TARGET_SAFE_RADIUS

    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y, self.radius, self.radius,
                                     TARGET_SAFE_COLOR, 90)

    def hit(self):
        self.alive = False
        return -10


class BearTarget(Target):
    """
    4
    just for fun
    """
    def __init__(self):
        super().__init__()
        self.center.x = SCREEN_WIDTH
        self.center.y = SCREEN_HEIGHT
        self.velocity.dx = -3
        self.velocity.dy = -2
        self.lives = 10
        self.radius = TARGET_RADIUS * 3

    def draw(self):
        arcade.draw_ellipse_outline\
            (self.center.x, self.center.y, TARGET_RADIUS * 3, TARGET_RADIUS * 4,
            arcade.color.BROWN, 6, 90)
        text = "BEAR"
        arcade.draw_text(text, self.center.x - 60, self.center.y - 30, arcade.color.BROWN, 40)

    def hit(self):
        """
        It takes 5 bullets to kill the bear, and it brings 10 scores only if the bear is killed
        :return: 
        """
        if self.lives > 1:
            self.lives -= 1
            return 0
        else:
            self.alive = False
            return 10

class Rifle:
    """
    The rifle is a rectangle that tracks the mouse.
    """
    def __init__(self):
        self.center = Point()
        self.center.x = 0
        self.center.y = 0

        self.angle = 45

    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y, RIFLE_WIDTH, RIFLE_HEIGHT,
                                     RIFLE_COLOR, self.angle)


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Rifle
        Target (and it's sub-classes)
        Point
        Velocity
        Bullet
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class, but mostly
    you shouldn't have to. There are a few sections that you
    must add code to.
    """
    """
    By Yurii Vasiuk
    I am adding the functionality for keeping track of the bullets
    and recharging the cartridge
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)

        self.rifle = Rifle()
        self.score = 0

        self.bullets = []

        # added by Yurii Vasiuk
        self.cartridge = 30

        # TODO: Create a list for your targets (similar to the above bullets)
        self.targets = []

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # draw each object
        self.rifle.draw()

        for bullet in self.bullets:
            bullet.draw()

        # TODO: iterate through your targets and draw them...
        for target in self.targets:
            target.draw()

        self.draw_score()

        # added by Yurii Vasiuk
        self.draw_cartridge()
        if (self.cartridge == 0):
            self.draw_recharge_message()

    def draw_score(self):
        """
        Puts the score on the screen,
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text\
            (score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.NAVY_BLUE)

    def draw_cartridge(self):
        """
        draws the number of bullets in the cartridge
        :return: 
        """
        cartridge_text = "Bullets: {}".format(self.cartridge)
        start_x = 10
        start_y = SCREEN_HEIGHT - 40
        arcade.draw_text \
            (cartridge_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.NAVY_BLUE)

    def draw_recharge_message(self):
        """
        displays the recharge message 
        :return: 
        """
        recharge_text = "No bullets.\nRecharge will cost you 5 points. "
        recharge_confirm = "\nClick on the green rifle square to recharge."
        start_x = 40
        start_y = SCREEN_HEIGHT - 140
        arcade.draw_text \
            (recharge_text, start_x=start_x, start_y=start_y, font_size=20, color=arcade.color.RED)
        arcade.draw_text \
            (recharge_confirm, start_x=start_x, start_y=start_y-40, font_size=20, color=arcade.color.GREEN)
        arcade.draw_rectangle_filled(0, 0, 50, 50, color=arcade.color.GREEN)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_collisions()

        self.check_off_screen()

        # decide if we should start a target
        if random.randint(1, 50) == 1:
            self.create_target()

        for bullet in self.bullets:
            bullet.advance()

        # TODO: Iterate through your targets and tell them to advance
        for target in self.targets:
            target.advance()

    def create_target(self):
        """
        Creates a new target of a random type and adds it to the list.
        :return:
        """

        # TODO: Decide what type of target to create and append it to the list
        number = random.randint(1, 5)
        if number == 1 or number == 2 or number == 3:
            self.targets.append(StandardTarget())
        elif number == 4:
            self.targets.append(SafeTarget())
        elif number == 5:
            self.targets.append(StrongTarget())

        bear_random = random.randint(1, 20)
        if bear_random == 1:
            self.targets.append(BearTarget())


    def check_collisions(self):
        """
        Checks to see if bullets have hit targets.
        Updates scores and removes dead items.
        :return:
        """

        # NOTE: This assumes you named your targets list "targets"

        for bullet in self.bullets:
            for target in self.targets:

                # Make sure they are both alive before checking for a collision
                if bullet.alive and target.alive:
                    too_close = bullet.radius + target.radius

                    if (abs(bullet.center.x - target.center.x) < too_close and
                                abs(bullet.center.y - target.center.y) < too_close):
                        # its a hit!
                        bullet.alive = False
                        self.score += target.hit()

                        # We will wait to remove the dead objects until after we
                        # finish going through the list

        # Now, check for anything that is dead, and remove it
        self.cleanup_zombies()

    def cleanup_zombies(self):
        """
        Removes any dead bullets or targets from the list.
        :return:
        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for target in self.targets:
            if not target.alive:
                self.targets.remove(target)

    def check_off_screen(self):
        """
        Checks to see if bullets or targets have left the screen
        and if so, removes them from their lists.
        :return:
        """
        for bullet in self.bullets:
            if bullet.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.bullets.remove(bullet)

        for target in self.targets:
            if target.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.targets.remove(target)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        # set the rifle angle in degrees
        self.rifle.angle = self._get_angle_degrees(x, y)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # Fire!
        angle = self._get_angle_degrees(x, y)

        bullet = Bullet()

        """
        Added by Yurii Vasiuk
        The logic to keep track of the number of the bullets and recharge the cartridge if needed
        """
        if (self.cartridge > 0):
            bullet.fire(angle)
            self.cartridge -= 1
        else:
            # This functionality is added to handle the recharge
            position = Point(x, y)
            if (position.x < 50 and position.y < 50):
                self.cartridge = 30
                self.score -= 5

        self.bullets.append(bullet)

    def _get_angle_degrees(self, x, y):
        """
        Gets the value of an angle (in degrees) defined
        by the provided x and y.
        Note: This could be a static method, but we haven't
        discussed them yet...
        """
        # get the angle in radians
        angle_radians = math.atan2(y, x)

        # convert to degrees
        angle_degrees = math.degrees(angle_radians)

        return angle_degrees

# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()