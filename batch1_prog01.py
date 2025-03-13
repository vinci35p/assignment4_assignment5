# Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.

# Input function and variable.

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

# Using f string to the print function with max function to deter bigger number.

print(f"The bigger number is {max(num1, num2)}.")