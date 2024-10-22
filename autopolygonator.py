# Polygonator works by taking the sides as the range and
# "l" being the side length and then uses those two factors to
# determine when to stop drawing and how many sides to draw.
# The 360 degrees used for a circle is divided by the
# number of sides giving us the correct angles or the polygon
#
# ex: 360 / 4 = 90 (4 sides in a square ) 90 is a perfect right triangle
# which creates the square.


import turtle
s = int( input("Sides: "))
length = int (input("Total Length: "))
l = length / s
my_screen = turtle.getscreen ()
my_turtle = turtle.Turtle()
my_turtle.pensize(5)
my_turtle.pencolor("red")

for x in range (s):
    my_turtle.forward(l)
    my_turtle.right(360 / s)
        
        
    
