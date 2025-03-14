# Sum, input and loop function stored in the variable.
total = sum(int(input(f"Enter number {i + 1}: ")) for i in range(10))

# Print the resultant.
print(f"The sum is {total}.")