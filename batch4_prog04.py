# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function:

# Input a number.
num_list = []

while True:
    try:
        num = int(input("Enter a number: "))
        num_list.append(num)

# Determine numbers from highest to lowest.
    except ValueError:
        if num_list:
            num_list.sort()

# Print numbers from highest to lowest.
            print(f"The numbers from lowest to highest are: {num_list}")
        else:
            print("No valid entry inputted.")
        break