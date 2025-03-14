# Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

# Input 10 numbers, and count even numbers.
even_numbers = sum(1 for i in range(10) if int(input(f"Enter number {i + 1}: ")) % 2 == 0)

# Print the count amount.
print(f"The number of even numbers is {even_numbers}.")