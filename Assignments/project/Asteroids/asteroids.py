"""
File: asteroids.py
Original Author: Br. Burton
Designed to be completed by others
This program implements the asteroids game.
"""
import math
from project.Asteroids.asteroids_classes import *

# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_WIDTH_EXTENDED = 1200

class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.held_keys = set()

        # TODO: declare anything here you need the game class to track
        self.asteroids = []
        self.ship = Ship()
        self.bullets = []
        self.game_over = True
        # the variables to keep track of the game statistics
        self.num_ships = 1
        self.num_rocks = 0
        # the score is a proportions of destroyed rocks per used ships
        self.score = 0

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()

        if self.game_over == True or not self.asteroids:
            self.start_game()

        #if self.game_over == False:
        # TODO: Tell everything to advance or move forward one step in time
        for asteroid in self.asteroids:
            asteroid.advance()
            asteroid.wrap(SCREEN_WIDTH, SCREEN_HEIGHT)

        # the ship is advancing based on the thrust and rear_thrust calculations;
        # those are defined in the Ship class and called in the "check_keys"
        self.ship.advance()
        self.ship.wrap(SCREEN_WIDTH, SCREEN_HEIGHT)

        # bullets' lives are handled (keep advancing and wrapping until the death time)
        for bullet in self.bullets:
            bullet.advance()
            bullet.wrap(SCREEN_WIDTH, SCREEN_HEIGHT)
            if bullet.lives == 0:
                self.bullets.remove(bullet)

        # TODO: Check for collisions
        self.check_collisions()

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        self.draw_game_statistics()

        # TODO: draw each object
        for asteroid in self.asteroids:
            asteroid.draw()

        self.ship.draw()

        for bullet in self.bullets:
            bullet.draw()

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            self.ship.turn_left()

        if arcade.key.RIGHT in self.held_keys:
            self.ship.turn_right()

        if arcade.key.UP in self.held_keys:
            self.ship.thrust()

        if arcade.key.DOWN in self.held_keys:
            self.ship.rear_thrust()

        # Machine gun mode...
        # if arcade.key.SPACE in self.held_keys:
            # pass

    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                # TODO: Fire the bullet here!
                bullet = Bullet()
                bullet.fire(self.ship)
                self.bullets.append(bullet)

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)

    """
    Methods added by Yurii Vasiuk
    """
    def start_game(self):
        """
        START OF THE GAME creating necessary objects
        :return: 
        """
        # 1 Create 5 big asteroids accordingly to the game specification
        for i in range(0, 5):
            # get random point for each big asteroid
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
            point = Point(x, y)
            # get random direction angle for each big asteroid
            # and calculate the velocity based on that
            direction_angle = random.randint(0, 360)
            dx = math.cos(math.radians(direction_angle)) * BIG_ROCK_SPEED
            dy = math.sin(math.radians(direction_angle)) * BIG_ROCK_SPEED
            velocity = Velocity(dx, dy)
            # make the big asteroid
            self.asteroids.append(BigAsteroid(point, velocity))

        # 2 Create a new ship to replace the old one
        self.ship = Ship()

        self.game_over = False

    def check_collisions(self):
        """
        check all objects of the game for collision
        and in the case of collision call the hit functions for each object
        :return: 
        """
        # loop 1 -- for each asteroid
        for asteroid in self.asteroids:
            # a) collision with the ship
            collision_distance = asteroid.radius + self.ship.radius
            if (abs(asteroid.center.x - self.ship.center.x) < collision_distance and
                        abs(asteroid.center.y - self.ship.center.y) < collision_distance):
                # the ship is dead, the game is over
                self.ship.hit()
                self.num_ships += 1
                self.score = int(self.num_rocks / self.num_ships)
            # loop 2 -- for each bullet
            for bullet in self.bullets:
                if (abs(asteroid.center.x - bullet.center.x) < collision_distance and
                            abs(asteroid.center.y - bullet.center.y) < collision_distance):
                    bullet.hit()
                    asteroid.hit()
                    self.explode(asteroid)
                    self.num_rocks += 1
                    self.score = int(self.num_rocks / self.num_ships)

        # finally, clean up all dead objects
        self.remove_dead_objects()

    def remove_dead_objects(self):
        # 1 (the ship is killed, so clear all asteroids and all bullets
        #    and restart the game by assigning True to the "game_over")
        if self.ship.alive == False:
            self.asteroids.clear()
            self.bullets.clear()
            self.game_over = True
        # 2 loop through the bullets and the asteroids and remove the dead ones
        for bullet in self.bullets:
            if bullet.alive == False:
                self.bullets.remove(bullet)
        # 3 loop through the asteroids and remove the dead ones
        for asteroid in self.asteroids:
            if asteroid.alive == False:
                self.asteroids.remove(asteroid)

    def explode(self, asteroid):
        """
        append the fractions of the exploded asteroid to the list of asteroids
        as newly created asteroids defined in the "asteroid_classes.py"
        :param asteroid: 
        :return: 
        """
        asteroid.break_apart()
        for fraction in asteroid.fractions:
            self.asteroids.append(fraction)

    def draw_game_statistics(self):
        """
        draw the game stats in the designated right part of the screen
        (between "SCREEN_WIDTH" AND "SCREEN_WIDTH_EXTENDED"
        :return: 
        """
        arcade.draw_text \
            ("GAME STATISTICS", start_x=SCREEN_WIDTH + 80, start_y=SCREEN_HEIGHT - 50,
             font_size=30, color=arcade.color.RED)
        arcade.draw_text \
            ("Rocks destroyed: {}".format(self.num_rocks),
             start_x=SCREEN_WIDTH + 100, start_y=SCREEN_HEIGHT - 100,
             font_size=20, color=arcade.color.RED)
        arcade.draw_text \
            ("Ships used: {}".format(self.num_ships),
             start_x=SCREEN_WIDTH + 100, start_y=SCREEN_HEIGHT - 150,
             font_size=20, color=arcade.color.RED)
        arcade.draw_text \
            ("The score: {}".format(self.score),
             start_x=SCREEN_WIDTH + 100, start_y=SCREEN_HEIGHT - 200,
             font_size=20, color=arcade.color.RED)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH_EXTENDED, SCREEN_HEIGHT)
arcade.run()