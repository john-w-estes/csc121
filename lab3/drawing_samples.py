"""
I am writing some comments about this particular file.
"""
# Importing the 'arcade' library
import arcade

#open a window
arcade.open_window(600, 600, "Drawing Example")

#set background color

# name color by name
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

#"""name color by RGB number
#arcade.set_background_color((100,55,180))
#"""

#get ready to Drawing
arcade.start_render()

#draw a rectangle
#left of 5, right of 35
#top of 590, bottom of 570
arcade.draw_lrtb_rectangle_filled(5,35,590,570,arcade.color.BITTER_LIME)

#different way to draw a rectangle
#center rectangle at (100, 520) with a width of 45 and a height of 25
arcade.draw_rectangle_filled(100,520,45,25, arcade.color.BLUSH)

#rotate a rectangle
#center a rectangle at (200,520) with a width of 45 and a height of 25
#also, rotate it 45 degrees
arcade.draw_rectangle_filled(200,520,45,25, arcade.color.BLUSH, 45)

#draw a point at (50, 580) that is 5 pixels large
arcade.draw_point(50, 580, arcade.color.RED, 5)

#draw a line
#start at point (75, 590)
#end at point (95, 570)
arcade.draw_line(75, 590, 95, 570, arcade.color.BLACK, 2)

#draw a circle outline centered at (140, 580) with a radius of 18 and a draw_line
#width of 3
arcade.draw_circle_outline(140, 580, 18, arcade.color.WISTERIA, 3)

#draw a circle centered at (190, 580) with a radius of 18
arcade.draw_circle_filled(190,580,18,arcade.color.WISTERIA)

#draw an ellipse. Centered at (240, 580) with a width of 30
#and a height of 15
arcade.draw_ellipse_filled(240, 580, 30, 15, arcade.color.AMBER)

#draw text starting at (10, 450) with a size of 20 points.
arcade.draw_text("Simpson College", 10, 450, arcade.color.BRICK_RED, 20)

#draw a bitmap
arcade.draw_text("draw_bitmap", 483, 3, arcade.color.BLACK, 12)
texture = arcade.load_texture(":resources:images/space_shooter/playerShip1_orange.png")
scale = .6
arcade.draw_texture_rectangle(540, 120, scale * texture.width,
                              scale * texture.height, texture, 0)
arcade.draw_texture_rectangle(540, 60, scale * texture.width,
                              scale * texture.height, texture, 45)



#finish Drawing
arcade.finish_render()


#keep the window open until someone closes it
arcade.run()
