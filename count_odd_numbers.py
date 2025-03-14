# Input 10 numbers, count odd numbers.
odd_numbers = sum(1 for i in range(10) if int(input(f"Enter number {i + 1}: ")) % 2 != 0)

# Print the counted odd numbers for the given input numbers.
print(f"The number of odd numbers are {odd_numbers}.")