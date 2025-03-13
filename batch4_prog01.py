# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

# Input 10 numbers.
num_list = [int(input(f"Enter number {i + 1}: ")) for i in range(10)]

# Determine the numbers that have duplicate.
duplicate_num = {num for num in num_list if num_list.count(num) > 1}

# Print the numbers.
print(f"The duplicate numbers are: {duplicate_num}.")
