import arcade

def draw_section_outlines():
    color = arcade.color.BLACK

    #Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, color)
    arcade.draw_rectangle_outline(450, 150, 300, 300, color)
    arcade.draw_rectangle_outline(750, 150, 300, 300, color)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, color)

    #Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, color)
    arcade.draw_rectangle_outline(450, 450, 300, 300, color)
    arcade.draw_rectangle_outline(750, 450, 300, 300, color)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, color)

#First section
def draw_section_1():
    for row in range(30):
        for col in range(30):
            x = 10 * (row + .5)
            y = 10 * (col + .5)
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

#Second section
def draw_section_2():
    for row in range(30):
        for col in range(30):
            x = 300 + 10 * (row + .5)
            y = 10 * (col + .5)
            if (row)%2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)

#Third section
def draw_section_3():
    for row in range(30):
        for col in range(30):
            x = 600 + 10 * (row + .5)
            y = 10 * (col + .5)
            if (col)%2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)

#Fourth Section
def draw_section_4():
    for row in range(30):
        for col in range(30):
            x = 900 + 10 * (row + .5)
            y = 10 * (col + .5)
            if row%2 != 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
            elif row%2 == 0 and col%2 == 0:
                    arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            else:
                    arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)

#Firth Section
def draw_section_5():
    for row in range(30):
        for col in range(row):
            x = 10 * (row + .5)
            y = 300 + 10 * (col + .5)
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

#Sixth Section
def draw_section_6():
    for row in range(30):
        for col in range(30-row):
            x = 300 + 10 * (row + .5)
            y = 300 + 10 * (col + .5)
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

#Seventh Section
def draw_section_7():
    for row in range(31):
        for col in range(row):
            x = 600 + 10 * (col + .5)
            y = 300 + 10 * (row + .5)
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

#Eighth Section
def draw_section_8():
    for row in range(30):
        for col in range(row):
            x = 900 + 10 * (29 - col + .5)
            y = 300 + 10 * (row + .5)
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def main():
    #Create a window
    arcade.open_window(1200, 600, "Lab 06 -- Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    #Draw the outlines for the sections
    draw_section_outlines()

    #Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()

if __name__=='__main__':
    main()
