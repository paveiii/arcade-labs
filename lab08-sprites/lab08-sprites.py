import arcade
from arcade import draw_polygon_filled, draw_rectangle_filled
from arcade import ShapeElementList

import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5
DEAD_ZONE = 0.35

score = 0
score_points_list = []

def draw_fire(p1,p2, color):
    arcade.draw_line(p1 + (random.randint(-400,400)), (random.randint(-300,300)), p2 + (random.randint(1,300)), (random.randint(1,600)), color, random.randint(1,12))

def create_entities(count:int, lista, spriteName, scale, maxRandomAngle):
    for i in range(count):
        entity = arcade.Sprite(spriteName, scale, angle=random.randrange(0,maxRandomAngle))

        # Position the coin
        entity.center_x = random.randrange(SCREEN_WIDTH)
        entity.center_y = random.randrange(SCREEN_HEIGHT)

        # Add the coin to the lists
        lista.append(entity)
class Jacket:
    def __init__(self, position_x, position_y, change_x, change_y):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.sprite = arcade.Sprite("SprJacketHM1.webp", scale = 0.2, center_x=position_x, center_y=position_y)
    def on_update(self):
        self.sprite.position = [self.position_x, self.position_y]
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < 50:
            self.position_x = 50

        if self.position_x > SCREEN_WIDTH - 50:
            self.position_x = SCREEN_WIDTH - 50

        if self.position_y < 25:
            self.position_y = 25

        if self.position_y > SCREEN_HEIGHT - 25:
            self.position_y = SCREEN_HEIGHT - 25

class Mobster:
    def __init__(self, position_x, position_y, change_x=0, change_y=0):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.sprite = arcade.Sprite("HM1sprRussianGangster.webp", scale = 0.3, center_x=position_x, center_y=position_y)
        self.changeTimer = 0
    def on_update(self):
        self.changeTimer -= 1
        self.sprite.position = [self.position_x, self.position_y]
        self.position_y += self.change_y
        self.position_x += self.change_x
        if(self.changeTimer <= 0):
            self.new_direction()
        self.on_bounds()

    def new_direction(self):
        self.change_x = random.randrange(-5,5)
        self.change_y = random.randrange(-5, 5)
        self.changeTimer = random.randint(250,500)
    def on_bounds(self):
        if self.position_x < 50:
            self.change_x *= -1

        if self.position_x > SCREEN_WIDTH - 50:
            self.change_x *= -1

        if self.position_y < 25:
            self.change_y *= -1

        if self.position_y > SCREEN_HEIGHT - 25:
            self.change_y *= -1


class MyGame(arcade.Window):
    def __init__(self):

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 8")

    def setup(self):
        self.jacket = Jacket(300, 300, 0, 0)
        self.points = arcade.SpriteList()
        self.enemies_sprites = arcade.SpriteList()
        self.enemies = []
        self.score = 0
        create_entities(50, self.points, "pixel-cig32x.png", 0.75, 360)


        for i in range(10):
            mobster = Mobster(random.randrange(SCREEN_WIDTH),random.randrange(SCREEN_HEIGHT))
            self.enemies.append(mobster)
            self.enemies_sprites.append(mobster.sprite)

    def on_draw(self):
        self.clear()
        arcade.set_background_color(arcade.color.ASH_GREY)
        draw_fire(0,800,arcade.color.BURNT_ORANGE)
        self.points.draw()
        self.enemies_sprites.draw()
        self.jacket.sprite.draw()
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)


    def on_update(self, delta_time: float):
        self.jacket.on_update()
        for enemy in self.enemies:
            enemy.on_update()
        self.points.update()
        points_hit_list = arcade.check_for_collision_with_list(self.jacket.sprite, self.points)
        for point in points_hit_list:
            point.remove_from_sprite_lists()
            self.score += 1

        self.enemies_sprites.update()
        points_hit_list = arcade.check_for_collision_with_list(self.jacket.sprite, self.enemies_sprites)
        for point in points_hit_list:
            point.remove_from_sprite_lists()
            self.score -= 1
            for i in range(2):
                mobster = Mobster(random.randrange(SCREEN_WIDTH), random.randrange(SCREEN_HEIGHT))
                self.enemies.append(mobster)
                self.enemies_sprites.append(mobster.sprite)

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.jacket.change_x += -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.jacket.change_x += MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.jacket.change_y += MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.jacket.change_y += -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.jacket.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.jacket.change_y = 0
def main():
    window = MyGame()
    window.setup()
    arcade.run()

main()