# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.

# Input a number.
number = []
while True:
    try:
        num = int(input("Enter a number: "))

# Print if number is duplicate.
        if num in number:
            print("Duplicate.")

# Print if number is unique.
        else:
            print("Unique")
            number.append(num)

# Print if number is invalid then end the program.
