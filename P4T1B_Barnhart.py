# Turtle Graphic using a Loop
# 24MAR2020
# CTI-110
# Anthony Barnhart

import turtle
wn = turtle.Screen()
ab = turtle.Turtle()
turtle.speed(1)

#Draw Initials

ab.forward(50)
ab.left(90)
ab.backward(50)
ab.forward(100)
ab.left(90)
ab.forward(50)
ab.left(90)
ab.forward(100)
ab.penup()
ab.goto(100,0)
ab.pendown()
ab.forward(50)
ab.backward(100)
ab.left(90)
ab.forward(50)
ab.right(90)
ab.forward(50)
ab.right(90)
ab.forward(50)
ab.backward(50)
ab.left(90)
ab.forward(50)
ab.right(90)
ab.forward(50)

# Pseudocode for the above code.
# Setup Turtle
# Draw first initial of "A"
# Tell Turtle to pick up pen and move
# Draw second initial of "B"
