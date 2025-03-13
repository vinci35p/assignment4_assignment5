# Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

# Input a number.
num_list = []

while True:
    try:
        num = int(input("Enter a number: "))
        num_list.append(num)

    except ValueError:
        break

# Determine the most iterated number inputted.
if not num_list:
    print("No numbers are entered.")
else:
    iteration = {}
    for num in num_list:
        if num in iteration:
            iteration[num] += 1

    most_iterated_num = max(iteration, key=iteration.get)
    most_count = iteration[most_iterated_num]

# Print the number.

    print(most_iterated_num)