import arcade
from arcade import draw_polygon_filled, draw_rectangle_filled
from arcade import ShapeElementList

import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5

def draw_fire(p1,p2, color):
    arcade.draw_line(p1 + (random.randint(-400,400)), (random.randint(-300,300)), p2 + (random.randint(1,300)), (random.randint(1,600)), color, random.randint(1,12))

def draw_jacket(x,y):
    draw_rectangle_filled(x, y, 400, 250, arcade.color.APRICOT, 0)
    draw_rectangle_filled(x, y, 250, 250, arcade.color.RED_BROWN, 0)
class Jacket:
    def __init__(self, position_x, position_y):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
    def draw(self):
        draw_jacket(self.position_x, self.position_y)
    def update_movement(self, change_x = None, change_y = None):
        if(change_y != None): self.position_y += change_y
        if(change_x != None):self.position_x += change_x

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

        self.jacket = Jacket(500,500)

    def on_draw(self):
        self.clear()
        arcade.set_background_color(arcade.color.ASH_GREY)
        draw_fire(0,800,arcade.color.BURNT_ORANGE)
        self.jacket.draw()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.jacket.update_movement(-MOVEMENT_SPEED)
        elif key == arcade.key.RIGHT:
            self.jacket.update_movement(MOVEMENT_SPEED)
        elif key == arcade.key.UP:
            self.jacket.update_movement(None,MOVEMENT_SPEED)
        elif key == arcade.key.DOWN:
            self.jacket.update_movement(None,-MOVEMENT_SPEED)

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.jacket.update_movement(0)
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.jacket.update_movement(None,0)



def main():
    window = MyGame()
    arcade.run()



main()