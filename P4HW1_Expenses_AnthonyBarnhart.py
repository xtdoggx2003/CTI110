# CTI-110
# P4HW1 - Expenses
# Anthony Barnhart
# 31MAR2020

# Initialize the accumulator.
account_balance = 0
ending_balance = 0
expense = 0
keep_going = "y"


# Prompt user for account balance.
account_balance = float (input("Enter the starting balance of the account you want to use:"))

# Set ending balance to be the starting balance at the beginning of the loop.
ending_balance = account_balance

# Calculate the balance.
for a in range (1000):    
    while keep_going == "y":

        # Prompt user for an expense.
        purchase = int (input("What is the value of the expense?:"))
        
        # Calculate the remaining balance.
        ending_balance = ending_balance - purchase

        # Calculate the total expenses entered.
        expense = expense + 1

        # Ask if user has another expense.
        keep_going = input("Do you have another expense? (Enter y for yes)")                       

if keep_going == "n":
    print("Amount in account before expense subtraction $", format (account_balance, ",.2f"))
    print("Number of expense entered:", expense)

    print("Amount in account AFTER expenses subracted is $", format (ending_balance, ",.2f"))

# Psuedo Code

# Prompt user to enter ammount in account in which money will be withdran from
# Prompt user to enter amount of first expense
# Subtract expense from account
# Ask user if they would like to add another expense
    # If "yes" then ask user to add expense
    # If "no" then display the following
        # Amount in account BEFORE expenses
        # Number of transactions made
        # Amount in account AFTER all expenses are subtracted
        
