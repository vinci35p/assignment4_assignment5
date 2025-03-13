# Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

# Input a number.
num_list = []

while True:
    try:
        num = int(input("Enter a number: "))

    except ValueError:
        break

# Determine the most iterated number inputted.

# Print the number.