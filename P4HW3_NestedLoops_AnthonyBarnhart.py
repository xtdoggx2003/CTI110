# Using Nested Loops To Draw an Angle.
# 07APR20
# CTI-110 P4HW3 - Nested Loops
# Anthony Barnhart
#

# Create the loop.

col = 15

for row in range (col):
    print ("#", end="", sep="")
    for spaces in range (row):
        print (" ", end="", sep="")
    print ("#", sep="")

# Pseudo Code

# Determine how many rows you want
# Determine how many colums you want to print
# Set the outter loop of starting with the "#"
# Set the inner loop for the spaces required between "#"
