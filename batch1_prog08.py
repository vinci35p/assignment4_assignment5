# Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

# Input 10 numbers, count odd numbers.
odd_numbers = sum(1 for i in range(10) if int(input(f"Enter number {i + 1}: ")) % 2 != 0)

# Print the counted odd numbers for the given input numbers.
