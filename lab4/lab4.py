import arcade


screen_width = 800
screen_height = 600




def draw_grid():
    for i in range(0,6):
        arcade.draw_line(0, 100*i, 800, 100*i, arcade.color.BLACK)
        arcade.draw_text(str(100*i), 10, 100*i, arcade.color.BRICK_RED, 12)
    for i in range(0,8):
        arcade.draw_line(100*i, 0, 100*i, 600, arcade.color.BLACK)
        arcade.draw_text(str(100*i), 100*i, 10, arcade.color.BRICK_RED, 12)

#drawing tables
def draw_table(y):
    #rectangle for desk and shadow
    arcade.draw_lrtb_rectangle_filled(0, 600, y+30, y+20,
        arcade.color.BLACK)
    arcade.draw_lrtb_rectangle_filled(0, 600, y+100 , y+30,
        arcade.color.DARK_GRAY)
    arcade.draw_lrtb_rectangle_filled(0, 600, y+20, y,
            arcade.color.CHARCOAL)

#drawing a computer:
def draw_computer(x,y):
    #CPU with lights
    arcade.draw_rectangle_filled(x-70,y+50,50,20,
        arcade.color.SILVER)
    arcade.draw_rectangle_filled(x-70,y+62,10,5,
        arcade.color.BLACK)
    arcade.draw_point(x-50, y+55, arcade.color.RED, 4)
    arcade.draw_point(x-50, y+50, arcade.color.BLUE, 4)
    arcade.draw_point(x-55, y+55, arcade.color.NEON_GREEN, 4)
    arcade.draw_rectangle_filled(x-85,y+50,10,10,
        arcade.color.OLD_SILVER)
    #monitor (two nestled rectangles)
    arcade.draw_rectangle_filled(x-70,y+85,50,40,
        arcade.color.SILVER)
    arcade.draw_rectangle_filled(x-70,y+85,50-5,40-5,
        arcade.color.SILVER_LAKE_BLUE)

#draw a chair
def draw_chair(x,y):
    #chair
    arcade.draw_line(x-40, y-50, x-40, y,
        arcade.color.BLACK, 5)
    arcade.draw_line(x-60, y-50, x-20, y-50,
        arcade.color.BLACK, 5)
    #wheels
    arcade.draw_circle_filled(x-40, y-55, 5,
        arcade.color.BLACK)
    arcade.draw_circle_filled(x-60, y-55, 5,
        arcade.color.BLACK)
    arcade.draw_circle_filled(x-20, y-55, 5,
            arcade.color.BLACK)
    #chair back and seat
    arcade.draw_ellipse_filled(x-40, y+10, 50, 50,
        arcade.color.CADET)
    arcade.draw_ellipse_filled(x-40, y-30, 60, 25,
            arcade.color.CADET)

#draw all computers:
def draw_computers():
    for i in range(1,7):
        for j in range(1,4):
            draw_computer(100*i, 100+200*(j-1))

#draw all charis
def draw_chairs():
    for i in range(1,7):
        for j in range(1,4):
            draw_chair(100*i, 100+200*(j-1))


#draw student a
def draw_student_a(x, y):
    #neck,
    arcade.draw_line(x-45, y+60, x-45, y-40, arcade.color.BRITISH_RACING_GREEN , 7)
    #arm
    arcade.draw_line(x-45, y+30, x-75, y+20, arcade.color.BRITISH_RACING_GREEN, 6)
    arcade.draw_line(x-72, y+20, x-85, y+30, arcade.color.PEACH, 6)
    #leg
    arcade.draw_line(x-45, y-30, x-85, y-20, arcade.color.COOL_BLACK, 6)
    arcade.draw_line(x-83, y-20, x-83, y-60, arcade.color.COOL_BLACK, 6)
    #head and hat
    arcade.draw_circle_filled(x-45, y+60, 20,
        arcade.color.PEACH)
#    arcade.draw_line(x-45, y+71, x-85, y+71, arcade.color.CITRINE, 3)
#    arcade.draw_rectangle_filled(x-45, y+80, 40, 20,
#        arcade.color.BRITISH_RACING_GREEN)

#draw student b:
def draw_student_b(x, y):
    #neck,
    arcade.draw_line(x-45, y+60, x-45, y-40, arcade.color.BRITISH_RACING_GREEN , 7)
    #arm
    arcade.draw_line(x-45, y+30, x-75, y+20, arcade.color.BRITISH_RACING_GREEN, 6)
    arcade.draw_line(x-72, y+20, x-85, y+30, arcade.color.COFFEE, 6)
    #leg
    arcade.draw_line(x-45, y-30, x-85, y-20, arcade.color.COOL_BLACK, 6)
    arcade.draw_line(x-83, y-20, x-83, y-60, arcade.color.COOL_BLACK, 6)
    #head and hat
    arcade.draw_circle_filled(x-45, y+60, 20,
        arcade.color.COFFEE)
#    arcade.draw_line(x-45, y+71, x-85, y+71, arcade.color.CITRINE, 3)
#    arcade.draw_rectangle_filled(x-45, y+80, 40, 20,
#        arcade.color.BRITISH_RACING_GREEN)

#drawing David O'Gwynn:
def draw_David(x,y):
    arcade.draw_line(x, y, x, y-60, arcade.color.BARBIE_PINK, 7)
    #right arm
    arcade.draw_line(x, y-30, x+15, y-50, arcade.color.BARBIE_PINK, 5)
    arcade.draw_line(x+12, y-50, x+27, y-40, arcade.color.BARBIE_PINK, 5)
    #left arm
    arcade.draw_line(x, y-30, x-20, y-50, arcade.color.BARBIE_PINK, 5)
    arcade.draw_line(x-18, y-50, x-30, y-30, arcade.color.BARBIE_PINK, 5)
    #lower torse
    arcade.draw_line(x, y-60, x, y-70, arcade.color.BRIGHT_UBE, 7)
    arcade.draw_line(x, y-70, x+15, y-120, arcade.color.BRIGHT_UBE, 5)
    arcade.draw_line(x, y-70, x-15, y-120, arcade.color.BRIGHT_UBE, 5)
    #head and face
    arcade.draw_circle_filled(x, y, 20, arcade.color.PEACH)
    point_list = ((x+3, y-3),
              (x-22, y-3),
              (x-18, y-23),
              (x+19, y-16),
              (x+22, y),
              (x+19, y+16),
              (x, y+22),
              (x-20, y+25),
              (x-18, y+20),
              (x+3, y+10),
              (x+3, y-3))
    arcade.draw_polygon_filled(point_list, arcade.color.BISTRE_BROWN)
    arcade.draw_ellipse_filled(x-8, y+3, 11, 12, arcade.color.BLACK)
    arcade.draw_ellipse_filled(x-8, y+3, 10, 11, arcade.color.WHITE)
    arcade.draw_ellipse_filled(x-19, y+4, 11, 12, arcade.color.BLACK)
    arcade.draw_ellipse_filled(x-19, y+4, 10, 11, arcade.color.WHITE)
    arcade.draw_circle_filled(x-11, y-11, 3, arcade.color.BLACK)

def on_draw(delt_time):
    """Draw everything"""
    arcade.start_render()

    draw_table(100)
    draw_table(300)
    draw_table(500)

    #back wall
    arcade.draw_lrtb_rectangle_filled(0,800,600,570, arcade.color.BURLYWOOD)
    arcade.draw_lrtb_rectangle_filled(790,800,600,0, arcade.color.BURLYWOOD)
    #O'Gwynn's desk
    arcade.draw_lrtb_rectangle_filled(600, 650, 560, 470, arcade.color.DARK_BROWN)
    arcade.draw_lrtb_rectangle_filled(600, 650, 500, 470, arcade.color.BLACK)

    draw_computers()
    draw_student_a(100,100)
    draw_student_a(200,300)
    draw_student_b(200,500)
    draw_student_b(100,300)
    draw_student_a(400,300)
    draw_student_b(500,500)
    draw_student_a(600,500)
    draw_student_a(600,300)
    draw_student_b(500,100)
    draw_chairs()
    draw_David(700, on_draw.david%600)

    on_draw.david -= 10

#    draw_grid()

on_draw.david = 450

def main():

    arcade.open_window(screen_width,screen_height, "Lab 4 Assignment: Dr. O'Gwynn Flees")
    #arcade.set_background_color(arcade.color.BURLYWOOD)
    arcade.set_background_color(arcade.color.LIGHT_SLATE_GRAY)

    #Call on_draw every 100th of a second.
    arcade.schedule(on_draw, 1/(100))
    arcade.run()

main()
