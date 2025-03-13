# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number.

# Input a number and initialize the list.
lowest_number = None
while True:
    try:
        num = int(input("Enter a number: "))

# Determine the lowest number.

        if lowest_number is None or num < lowest_number:
            lowest_number = num

# Print invalid entry if the inputted value is not a number, while printing the lowest number.
    except ValueError:
        if lowest_number is not None:
            print(f"The lowest number is {lowest_number}.")
        else:
            print("No valid numbers are inputted.")
        break



