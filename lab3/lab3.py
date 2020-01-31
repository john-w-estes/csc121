#import arcade
import arcade

#open a open
arcade.open_window(800,500, "Lab 3 Assignment")

#set background color
#arcade.set_background_color(arcade.color.RED)
arcade.set_background_color(arcade.color.BURLYWOOD)

#get ready to draw
arcade.start_render()

#rectangle for carpet
arcade.draw_lrtb_rectangle_filled(0,800,100,0,
    arcade.color.CHARCOAL)

#rectangle for desk
arcade.draw_lrtb_rectangle_filled(0,800,210,200,
    arcade.color.BLACK)

#variables for coordinates for computers and guy-in-chair
x1=100
x2=400
x3=700
x_guy=500
body_width=10
monitor_delta=25

#computer 1 centered along x = x1

#CPU with lights
arcade.draw_rectangle_filled(x1,235,180,50,
    arcade.color.SILVER)
arcade.draw_rectangle_filled(x1,(260+265)/2,50,5,
    arcade.color.BLACK)
arcade.draw_point(x1+70, 250, arcade.color.RED, 5)
arcade.draw_point(x1+70, 240, arcade.color.BLUE, 5)
arcade.draw_point(x1+60, 250, arcade.color.NEON_GREEN, 5)
arcade.draw_rectangle_filled(x1-70,235,30,30,
    arcade.color.OLD_SILVER)

#monitor (two nestled rectangles)
arcade.draw_rectangle_filled(x1,335,180,140,
    arcade.color.SILVER)
arcade.draw_rectangle_filled(x1,335,180-monitor_delta,140-monitor_delta,
    arcade.color.SILVER_LAKE_BLUE)

#computer 2 centered along x = x2

#CPU 2 with lights
arcade.draw_rectangle_filled(x2,235,180,50,
    arcade.color.SILVER)
arcade.draw_rectangle_filled(x2,(260+265)/2,50,5,
    arcade.color.BLACK)
arcade.draw_point(x2+70, 250, arcade.color.RED, 5)
arcade.draw_point(x2+70, 240, arcade.color.BLUE, 5)
arcade.draw_point(x2+60, 250, arcade.color.NEON_GREEN, 5)
arcade.draw_rectangle_filled(x2-70,235,30,30,
    arcade.color.OLD_SILVER)

#monitor 2 (two nestled rectangles)
arcade.draw_rectangle_filled(x2,335,180,140,
    arcade.color.SILVER)
arcade.draw_rectangle_filled(x2,335,180-monitor_delta,140-monitor_delta,
    arcade.color.SILVER_LAKE_BLUE)

#computer 3 centered along x = x3

#CPU 3 with lights
arcade.draw_rectangle_filled(x3,235,180,50,
    arcade.color.SILVER)
arcade.draw_rectangle_filled(x3,(260+265)/2,50,5,
    arcade.color.BLACK)
arcade.draw_point(x3+70, 250, arcade.color.RED, 5)
arcade.draw_point(x3+70, 240, arcade.color.BLUE, 5)
arcade.draw_point(x3+60, 250, arcade.color.NEON_GREEN, 5)
arcade.draw_rectangle_filled(x3-70,235,30,30,
    arcade.color.OLD_SILVER)

#monitor 3 (two nestled rectangles)
arcade.draw_rectangle_filled(x3,335,180,140,
    arcade.color.SILVER)
arcade.draw_rectangle_filled(x3,335,180-monitor_delta,140-monitor_delta,
    arcade.color.SILVER_LAKE_BLUE)

#rectangle for shadowing under desk
arcade.draw_lrtb_rectangle_filled(0,800,200,100,
    arcade.color.CAMEL)

#guy-in-chair
#neck,
arcade.draw_line(x_guy, 335, x_guy, 130, arcade.color.AMETHYST, body_width)
#shoe
arcade.draw_line(342, 50, 325, 50, arcade.color.BLAST_OFF_BRONZE, body_width)
#arm
arcade.draw_line(x_guy, 250, 410, 200, arcade.color.AMETHYST, body_width)
arcade.draw_line(414, 200, 350, 210, arcade.color.PEACH, body_width)
#leg
arcade.draw_line(x_guy, 130, 385, 135, arcade.color.AZURE, body_width)
arcade.draw_line(388, 135, 340, 50, arcade.color.AZURE, body_width)
#chair
arcade.draw_line(x_guy, 40, x_guy, 140,
    arcade.color.BLACK, body_width)
arcade.draw_line(x_guy-60, 40, x_guy+60, 40,
    arcade.color.BLACK, body_width)
#wheels
arcade.draw_circle_filled(x_guy,25,10,
    arcade.color.BLACK)
arcade.draw_circle_filled(x_guy-50,25,10,
    arcade.color.BLACK)
arcade.draw_circle_filled(x_guy+50,25,10,
        arcade.color.BLACK)
#chair back and seat
arcade.draw_ellipse_filled(x_guy, 190, 100, 110,
    arcade.color.CADET)
arcade.draw_ellipse_filled(x_guy, 100, 120, 60,
        arcade.color.CADET)
#head and hat
arcade.draw_circle_filled(x_guy, 325, 60,
    arcade.color.PEACH)
arcade.draw_line(x_guy, 335, x_guy-120, 335, arcade.color.CELADON_BLUE, body_width)
arcade.draw_rectangle_filled(x_guy, 360, 120, 60,
    arcade.color.CEIL)

#finish drawing
arcade.finish_render()
#open until closed by user
arcade.run()
