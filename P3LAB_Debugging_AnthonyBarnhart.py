# CTI-110
# P3LAB - Debugging
# Anthony Barnhart 
# 23MAR2020

# Get score from user.
Score = int(input("Enter the test score:"))

# Determine the "letter" grade based off of the score.
if Score >= 90 and Score <=100:
    print("Your grade is an A")
    
elif Score >= 80 and Score < 90:
    print("Your grade is a B")
    
elif Score >= 70 and Score < 80:
    print("Your grade is a C")

elif Score >=60 and Score < 70:
    print ("Your grade is a D")    
    
else:
    print("Your grade is an F")


# Pseudocode
# Ask user to score
# Calculate the "letter" grade based off of score
# Display the grade
