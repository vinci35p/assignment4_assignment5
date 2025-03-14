# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

# Input 10 numbers.
num_list = [int(input(f"Enter number {i + 1}: ")) for i in range(10)]

# Determine numbers who don't have a duplicate.
lone_numbers = [num for num in num_list if num_list.count(num) == 1]

# Print the lone numbers.
print(f"The lone numbers are: {lone_numbers}.")
