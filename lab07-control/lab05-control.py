import arcade
from arcade import draw_polygon_filled, draw_rectangle_filled
from arcade import ShapeElementList

import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5
DEAD_ZONE = 0.35

def draw_fire(p1,p2, color):
    arcade.draw_line(p1 + (random.randint(-400,400)), (random.randint(-300,300)), p2 + (random.randint(1,300)), (random.randint(1,600)), color, random.randint(1,12))

def draw_circle(x,y):
    arcade.draw_circle_filled(x,y,25,arcade.color.ANTIQUE_RUBY)
class Circle:
    def __init__(self, position_x, position_y):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
    def draw(self):
        draw_circle(self.position_x, self.position_y)
    def update_movement(self, change_x = None, change_y = None):
        if(change_y != None): self.position_y += change_y
        if(change_x != None):self.position_x += change_x

        if self.position_x < 25:
            self.position_x = 25

        if self.position_x > SCREEN_WIDTH - 25:
            self.position_x = SCREEN_WIDTH - 25

        if self.position_y < 25:
            self.position_y = 25

        if self.position_y > SCREEN_HEIGHT - 25:
            self.position_y = SCREEN_HEIGHT - 25


def draw_jacket(x,y):
    draw_rectangle_filled(x, y, 400, 250, arcade.color.APRICOT, 0)
    draw_rectangle_filled(x, y, 250, 250, arcade.color.RED_BROWN, 0)
class Jacket:
    def __init__(self, position_x, position_y, change_x, change_y):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
    def draw(self):
        draw_jacket(self.position_x, self.position_y)
    def on_update(self):
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < 200:
            self.position_x = 200

        if self.position_x > SCREEN_WIDTH - 200:
            self.position_x = SCREEN_WIDTH - 200

        if self.position_y < 125:
            self.position_y = 125

        if self.position_y > SCREEN_HEIGHT - 125:
            self.position_y = SCREEN_HEIGHT - 125


class MyGame(arcade.Window):
    def __init__(self):

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        self.jacket = Jacket(300,300,0,0)
        self.circle = Circle(300,300)

        joysticks = arcade.get_joysticks()

        if joysticks:
            self.joystick = joysticks[0]
            self.joystick.open()
        else:
            print("There are no joysticks.")
            self.joystick = None

    def on_draw(self):
        self.clear()
        arcade.set_background_color(arcade.color.ASH_GREY)
        draw_fire(0,800,arcade.color.BURNT_ORANGE)
        self.jacket.draw()
        self.circle.draw()
    def on_update(self, delta_time: float):
        if self.joystick:
            print(self.joystick.x, self.joystick.y)

            if abs(self.joystick.x) < DEAD_ZONE:
                self.circle.update_movement(0)
            else:
                self.circle.update_movement(self.joystick.x * MOVEMENT_SPEED)

            # Set a "dead zone" to prevent drive from a centered joystick
            if abs(self.joystick.y) < DEAD_ZONE:
                self.circle.update_movement(None, 0)
            else:
                self.circle.update_movement(None, -self.joystick.y * MOVEMENT_SPEED)
        self.jacket.on_update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.jacket.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.jacket.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.jacket.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.jacket.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.jacket.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.jacket.change_y = 0
def main():
    window = MyGame()
    arcade.run()

main()