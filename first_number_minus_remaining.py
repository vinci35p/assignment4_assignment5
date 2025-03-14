# Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

# Initialize number list variable.
number_list = []

# Input 10 numbers.
for num in range(10):
    num1 = int(input(f"Enter number {num + 1}: "))
    number_list.append(num1)

#Subtract the 1st number listed, then the rest of the remaining.
result = number_list[0] - sum(number_list[1:])

# Print the first number minus all the remaining numbers.
print(f"The result is {result}.")
