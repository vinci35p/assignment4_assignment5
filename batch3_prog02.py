# Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

# Input 10 numbers.
num_list = {int(input(f"Enter number {i + 1}: ")) for i in range(10)}

# Print the numbers.
print(f"The numbers are: {num_list}")