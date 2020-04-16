# Converting to Feet to Inches
# 16APR2020
# CTI-110 P5T2_FeetToInches
# Anthony Barnhart

# Constant for the number of inches per foot.

inches_per_foot = 12

# Main Function

def main():
    # Get the number of feet to convert.
    feet = int(input("Enter the number in feet:"))

    # Display the number converted to inches.
    print (feet, "equals", feet_to_inches(feet), "inches.")

# The feet_to_inches function converts feet to inches.
def feet_to_inches(feet):
    return feet * inches_per_foot

# Call the main function.
main()



#Pseudocode for the above program

# Ask for Feet input (main function)
# Convert Feet to Inches
# Display Inches
