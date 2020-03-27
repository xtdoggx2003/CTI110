# Turtle Graphic using a Loop
# 24MAR2020
# CTI-110
# Anthony Barnhart

import turtle

# Setup the turtle
turtle.speed(7
             )
turtle.hideturtle
side = side_unit = 50

# Draw the squares
for sq in range (1, 50 +1):
    turtle.goto(0,0)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    side = side_unit + 3 * sq

    turtle.goto(0,0)

# Create named constants for the corners.


# Pseudocode for the above code.

# Draw the 1st square
# Tell the turtle to offset each subsequent square
# Repeat the square until desired design is reached
