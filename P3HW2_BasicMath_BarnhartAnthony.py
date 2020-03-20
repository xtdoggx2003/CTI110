# CTI-110
# P3HW2 - BasicMath
# Anthony Barnhart 
# 18MAR2020


# Get user inputs for the requested variable outputs.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Get operation user wants to perform.

print("1. Add Numbers")
print("2. Multiply Numbers")
print("3. Subtract Numbers")
print("4. Exit")

choice = input("Choose Option:")

# Define what the designated output will be based off of user input.

if choice == "1":
    print(num1 + num2)

elif choice == "2":
    print(num1 * num2)

elif choice == "3":
    print(num1 - num2)

elif choice =="4":
    exit
    
else:
    print("Invalid Operation. Pick 1-4")

#Pseudocode for the above program

# Ask user to input 1st number
# Ask user to input 2nd number
# Ask user to pick what function they want to perform
# Calculate the output for the given function
# Display the result from the given function
