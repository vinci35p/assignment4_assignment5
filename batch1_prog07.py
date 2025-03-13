# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

# Sum, input and loop function stored in the variable.
total = sum(int(input(f"Enter number {i + 1}: ")) for i in range(10))

# Print the resultant.
print(f"The sum is {total}.")

