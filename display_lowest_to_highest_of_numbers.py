# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort()if function:

# Input a number.
num_list = []

while True:
    try:
        num = int(input("Enter a number: "))
        num_list.append(num)

# Determine the numbers from lowest to highest.
    except ValueError:
        if num_list:
            num_list.sort()

# Print the numbers from lowest to highest.
            print(f"The numbers from lowest to highest are: {num_list}")
        else:
            print("No valid entry inputted.")
        break