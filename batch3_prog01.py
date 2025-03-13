# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

# Input 10 numbers.
for i in range(10):
    num1 = [int(input(f"Enter number {i + 1}: "))]

# Determine numbers who don't have a duplicate.
    lone_numbers = [num for num in num1 if num1.count(num) == 1]

# Print the lone numbers.
    print(lone_numbers)