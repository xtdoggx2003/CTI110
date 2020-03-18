# CTI-110
# P3HW1 - Color Mixer
# Antony Barnhart
# 15MAR2020


# Get user input for primary color 1.
Prime1 = input("Enter first primary color of red, yellow or blue:")

# Get user input for primary color 2.
Prime2 = input("Enter second different primary color of red, yellow or blue:")


# Determine secondary color and error if not one of three listed colors
if Prime1 == "red" and Prime2 == "yellow" or Prime1 == "yellow" and Prime2 == "red":
    print("orange")
    
elif Prime1 == "blue" and Prime2 == "yellow" or Prime1 == "yellow" and Prime2 == "blue":
    print("green")
    
elif Prime1 == "blue" and Prime2 == "red" or Prime1 == "red" and Prime2 == "blue":
    print("purple")
    
else:
    print("error")


# Pseudocode
# Ask user to input prime color one
# Ask user to imput prime color two
# Only allow input of three colors Red, Yellow, Blue
# Determine the secondary color based off of user input
# Display secondary color
# Display error if any color outside of given perameters is input

    
