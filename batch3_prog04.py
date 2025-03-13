# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number.

# Input a number and initialize the list.
numbers = []
while True:
    try:
        num1 = int(input("Enter a number: "))

# Print invalid entry if the inputted value is not a number.
    except ValueError:
        print("Invalid entry.")

# Determine the lowest number from the inputted numbers.
        print(f"The lowest inputted number is {min(numbers)}.")

