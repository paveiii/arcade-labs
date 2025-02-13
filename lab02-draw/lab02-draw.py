import arcade
import random
from arcade import draw_polygon_filled, draw_rectangle_filled

arcade.open_window(800, 600, "Hola")

#JACKEEEEEEEEEEET
arcade.set_background_color(arcade.color.BLACK)
arcade.start_render()
draw_rectangle_filled(400,100,400,250,arcade.color.APRICOT,0)
draw_rectangle_filled(400,100,250,250,arcade.color.RED_BROWN,0)
arcade.draw_line(450, 125, 450, 175, arcade.color.APRICOT, 10)
arcade.draw_arc_outline(453, 159, 25, 25, arcade.color.APRICOT, 0, 180, 15, 270, 256)
arcade.draw_arc_outline(453, 141, 25, 25, arcade.color.APRICOT, 0, 180, 15, 270, 256)

mascaraPuntos1 = ((275,230),(375,200), (425,200),(525,230),(500,475),(450,550),(350,550),(300,475))
arcade.draw_polygon_filled(mascaraPuntos1, arcade.color.BEIGE)

mascaraPuntos2 = ((370,550),(400,575),(430,550),(425,400),(375,400))
arcade.draw_polygon_filled(mascaraPuntos2, arcade.color.ANTIQUE_RUBY)

arcade.draw_circle_filled(400,300,70,arcade.color.ANTIQUE_RUBY,225, 128)

mascaraPuntos3 = ((390,380),(410, 380),(435,300),(400,275),(365,300))
arcade.draw_polygon_filled(mascaraPuntos3, arcade.color.EARTH_YELLOW)

arcade.draw_point(350,375,arcade.color.BLACK,45)
arcade.draw_point(450,375,arcade.color.BLACK,45)
arcade.finish_render()


arcade.run()