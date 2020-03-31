# Bug Collector using Loops
# 29MAR2020
# CTI-110 P4T2 - Bug Collector
# Anthony Barnhart

# Initialize the accumlator.
total = 0

# Get the number of bugs collected for each day.
for day in range (1, 6):
    # Prompt the user.
    print("Enter number of bugs collected on day", day)

    # Input the number of bugs.
    bugs = int (input())

    # Add bugs to toal.
    total = total + bugs


# Display the total bugs.
print("You have collected a total of", total, "bugs")


# Psuedo Code
# Set total = 0
# For 5 days:
#   Input number of bugs collected for a day
#   Add bugs collected to total number of bugs
# Display the total bugs
