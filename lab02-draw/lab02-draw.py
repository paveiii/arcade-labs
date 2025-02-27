import arcade
import random
from arcade import draw_polygon_filled, draw_rectangle_filled
import random
def draw_jacket(muscles):
    draw_rectangle_filled(400, 100, 400 * muscles, 250 * muscles, arcade.color.APRICOT, 0)
    draw_rectangle_filled(400, 100, 250 * muscles, 250 * muscles, arcade.color.RED_BROWN, 0)
    arcade.draw_line(400, 0, 400, 400, arcade.color.DEEP_TAUPE, 15)
    arcade.draw_line(450, 100, 450, 175, arcade.color.APRICOT, 15)
    arcade.draw_arc_outline(453, 154, 35, 60, arcade.color.APRICOT, 0, 180, 15, 270, 256)
    arcade.draw_arc_outline(453, 121, 35, 60, arcade.color.APRICOT, 0, 180, 15, 270, 256)

    mascaraPuntos1 = ((275, 230), (375, 200), (425, 200), (525, 230), (500, 475), (450, 550), (350, 550), (300, 475))
    arcade.draw_polygon_filled(mascaraPuntos1, arcade.color.BEIGE)

    mascaraPuntos2 = ((370, 550), (400, 575), (430, 550), (425, 400), (375, 400))
    arcade.draw_polygon_filled(mascaraPuntos2, arcade.color.ANTIQUE_RUBY)

    arcade.draw_circle_filled(400, 300, 70, arcade.color.ANTIQUE_RUBY, 225, 128)

    mascaraPuntos3 = ((390, 380), (410, 380), (435, 300), (400, 275), (365, 300))
    arcade.draw_polygon_filled(mascaraPuntos3, arcade.color.EARTH_YELLOW)

    arcade.draw_point(350, 375, arcade.color.BLACK, 45)
    arcade.draw_point(450, 375, arcade.color.BLACK, 45)

def draw_ashes(x,y):
    arcade.draw_circle_filled(0+x, 0+y, random.randint(1,3), arcade.color.WHITE, 0, -1)
def draw_fire(p1,p2, color):
    arcade.draw_line(p1 + (random.randint(-400,400)), (random.randint(-300,300)), p2 + (random.randint(1,300)), (random.randint(1,600)), color, random.randint(1,12))
def pick_phrase():
    lista = ("I PUT THE NEW FORGIS ON THE JEEEP","DYING IS NOT AS SCARY AS IT SOUNDS","Well, let´s get this over with.","You'll never get the big picture","Bearing too much weight... Inevitably leads to the collapse of everything.","Maybe it wasn't so bad after all.","No worries man, it's on the house. You'd do the same for me, right?")
    return lista[random.randint(0,len(lista)-1)]
arcade.open_window(800, 600, "A Jacket")
arcade.set_background_color(arcade.color.ALABAMA_CRIMSON)

while(True):
    arcade.start_render()

    for i in range(1000):
        draw_ashes(random.randint(-400, 400), random.randint(-300, 300))
    for i in range(1000):
        draw_fire(random.randint(0, 800), random.randint(0, 600),arcade.color.ORANGE)
        draw_fire(random.randint(-50, 50), random.randint(0, 600),arcade.color.BURNT_ORANGE)
    draw_jacket(1.25)

    arcade.draw_text(pick_phrase(),random.randint(-400,400),random.randint(0,600), arcade.color.CATAWBA, random.randint(15,45))

    arcade.finish_render()

arcade.run()

