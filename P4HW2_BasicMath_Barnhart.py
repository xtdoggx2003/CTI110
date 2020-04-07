# CTI-110
# P4HW2 - BasicMath
# Anthony Barnhart 
# 5APR2020

# Define menu for ease of reference.

menu = """
1. Add Numbers
2. Mulitply Numbers
3. Subtract Numbers
4. Exit
"""
choice = None

# Start the loop.
while (choice !=4):
    # Get user inputs for the requested variable outputs.
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Call the menu for user selction and input.
    print(menu)

    # User selects their option for the 2 numbers.
    choice = int(input("Choose Option 1,2,3,4:"))

    if (choice == 1): # Addition option.
        print (num1, "+", num2, "=", num1+num2)

    elif (choice == 2): # Mulitiplication option.
        print (num1, "*", num2, "=", num1*num2)

    elif (choice == 3): # Subtraction option.
        print (num1, "-", num2, "=", num1-num2)

    elif (choice == 4): # User quit option.
        exit

    else:
        print ("Invalid Operation. Pick 1-4")
        

#Pseudocode for the above program

# Ask user to input 1st number
# Ask user to input 2nd number
# Ask user to pick what function they want to perform
# If user enters a number outside of 1-4, then return an error and ask to re-enter a number
# Program only terminates when 4 is selected
# Calculate the output for the given function
# Display the result from the given function
