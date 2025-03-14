# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

# Input a number.
num_list = []

while True:
    try:
        num = int(input("Enter a number: "))
        num_list.append(num)
    except ValueError:
        break

# Determine the average and print.
if num_list:
    average = sum(num_list) / len(num_list)
    print(f"The average for the inputted number is {average}.")
else:
    print("There are no valid inputted numbers.")