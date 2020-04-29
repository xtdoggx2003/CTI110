# Random Number Guessing Game
# 24APR2020
# CTI-110 P5HW1 - Random Number
# Anthony Barnhart

# Import the Random function.
import random

# Create variable to keep track of guesses
count = 0

# Define menu for ease of reference

def menu():
    print ("1. Play Game")
    print ("2. Exit")


choice = None

# Set the Loop
menu()
choice = int(input("Would you like to play a game?"))
    
while choice !=2:
    print ("Guess a number between 1 & 100:")
    x = random.randint (1, 100)

    while (True):
        guess = int(input())
        
        if guess == x:
            print ("Congratulations, you guessed the number in", count, "attempts!")
            menu()
            choice = int(input("Would you like to play a game?"))

        elif guess < x:
            print("Your guess is too low, try again:")
            count = count+1

        elif guess > x:
            print("Your guess is too high, try again:")
            count = count+1

        else:
            exit

if choice == 2:
    exit

        
#Pseudocode for the above program

# Ask user if they want to play the guessing game
# Randomly generate a number
# Ask user to guess and give hints (too low, too high)
# Generate a new random number each game
# Only quit when user selects to exit
