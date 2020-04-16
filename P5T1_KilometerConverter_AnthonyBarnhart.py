# Converting to Kilometers to Miles
# 16APR2020
# CTI-110 P5T1_KilometerConverter
# Anthony Barnhart

# Set global conversion factor

conversion_factor = 0.6214

# The main function gets a distance in kilometers and calls
# the show_miles function to convert it.

def main():
    # Get the distance in Kilometers.
    kilometers = float(input("Enter a distance in kilometers:"))

    # Display the distance converted to miles.
    show_miles(kilometers)

# The show_miles function converts the parameter km from
# kilometers to miles and displays the result.

def show_miles(km):
    #Calculate miles.
    miles = km * conversion_factor

    #Dislpay the miles.
    print (km, "kilometers equals", miles, "miles.")


# Call the main function.
main()



#Pseudocode for the above program

# Ask for Kilometer input (main function)
# Convert Kilometers to miles
# Display miles
