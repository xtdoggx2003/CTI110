# Basic Turtle Graphics Drawing
# 17FEB2020
# CTI-110 P2HW2 - Turtle Graphic
# Anthony Barnhart

import turtle

# Set window size
turtle.setup(500, 600)

# Setup the turtle
turtle.penup()
turtle.hideturtle()
turtle.speed(4)

# Create named constants for the corners.
LEFT_UPPER_X = -200
LEFT_UPPER_Y = 200

RIGHT_UPPER_X = 200
RIGHT_UPPER_Y = 200

MIDDLE_X = 0
MIDDLE_Y = 0

LEFT_BOTTOM_X = -200
LEFT_BOTTOM_Y = -200

RIGHT_BOTTOM_X = 200
RIGHT_BOTTOM_Y = -200

# Draw the dots for the corners and middle.
turtle.goto(LEFT_UPPER_X, LEFT_UPPER_Y)             #Left upper
turtle.dot()
turtle.goto(RIGHT_UPPER_X, RIGHT_UPPER_Y)           #Right upper
turtle.dot()
turtle.goto(MIDDLE_X, MIDDLE_Y)                     #Middle
turtle.dot()
turtle.goto(LEFT_BOTTOM_X, LEFT_BOTTOM_Y)           #Left bottom
turtle.dot()
turtle.goto(RIGHT_BOTTOM_X, RIGHT_BOTTOM_Y)         #Right bottom
turtle.dot()

#Draw a line from the left upper to left bottom.
turtle.goto(LEFT_UPPER_X, LEFT_UPPER_Y)
turtle.pendown()
turtle.goto(LEFT_BOTTOM_X, LEFT_BOTTOM_Y)
turtle.penup()

#Draw a line from the right upper to right bottom.
turtle.goto(RIGHT_UPPER_X, RIGHT_UPPER_Y)
turtle.pendown()
turtle.goto(RIGHT_BOTTOM_X, RIGHT_BOTTOM_Y)
turtle.penup()

#Draw a line from left upper to middle.
turtle.goto(LEFT_UPPER_X, LEFT_UPPER_Y)
turtle.pendown()
turtle.goto(MIDDLE_X, MIDDLE_Y)
turtle.penup()

#Draw a line from right upper to middle.
turtle.goto(RIGHT_UPPER_X, RIGHT_UPPER_Y)
turtle.pendown()
turtle.goto(MIDDLE_X, MIDDLE_Y)
turtle.penup()

#Draw a line from left bottom to middle.
turtle.goto(LEFT_BOTTOM_X, LEFT_BOTTOM_Y)
turtle.pendown()
turtle.goto(MIDDLE_X, MIDDLE_Y)
turtle.penup()

#Draw a line from the right bottom to middle.
turtle.goto(RIGHT_BOTTOM_X, RIGHT_BOTTOM_Y)
turtle.pendown()
turtle.goto(MIDDLE_X, MIDDLE_Y)
turtle.penup()

#Draw dotted line from upper left to upper right
turtle.goto(LEFT_UPPER_X, LEFT_UPPER_Y)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.forward(21)
turtle.pendown()
turtle.forward(120)
turtle.penup()
turtle.forward(21)
turtle.pendown()
turtle.forward(120)
turtle.penup()
turtle.forward(21)
turtle.pendown()
turtle.forward(50)
turtle.penup()

#Draw dotted line from bottom left to bottom right.
turtle.goto(LEFT_BOTTOM_X, LEFT_BOTTOM_Y)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.forward(21)
turtle.pendown()
turtle.forward(120)
turtle.penup()
turtle.forward(21)
turtle.pendown()
turtle.forward(120)
turtle.penup()
turtle.forward(21)
turtle.pendown()
turtle.forward(50)
turtle.penup()

# Pseudocode for the above code.

# Draw a dot at (LEFT_UPPER_X, LEFT_UPPER_Y)
# Draw a dot at (RIGHT_UPPER_X, RIGHT_UPPER_Y)
# Draw a dot at (MIDDLE_X, MIDDLE_Y)
# Draw a dot at (LEFT_BOTTOM_X, LEFT_BOTTOM_Y)
# Draw a dot at (RIGHT_BOTTOM_X, RIGHT_BOTTOM_Y)

# Draw a line from (LEFT_UPPER_X, LEFT_UPPER_Y) to (LEFT_BOTTOM_X, LEFT_BOTTOM_Y)
# Draw a line from (RIGHT_UPPER_X, RIGHT_UPPER_Y) to (RIGHT_BOTTOM_X, RIGHT_BOTTOM_Y)
# Draw a line from (LEFT_UPPER_X, LEFT_UPPER_Y) to (MIDDLE_X, MIDDLE_Y)
# Draw a line from (RIGHT_UPPER_X, RIGHT_UPPER_Y) to (MIDDLE_X, MIDDLE_Y)
# Draw a line from (LEFT_BOTTOM_X, LEFT_BOTTOM_Y) to (MIDDLE_X, MIDDLE_Y)
# Draw a line from (RIGHT_BOTTOM_X, RIGHT_BOTTOM_Y) to (MIDDLE_X, MIDDLE_Y)
# Draw a dashed line from (LEFT_UPPER_X, LEFT_UPPER_Y) to (RIGHT_UPPER_X, RIGHT_UPPER_Y)
# Draw a dashed line from (LEFT_BOTTOM_X, LEFT_BOTTOM_Y) to (RIGHT_BOTTOM_X, RIGHT_BOTTOM_Y)
