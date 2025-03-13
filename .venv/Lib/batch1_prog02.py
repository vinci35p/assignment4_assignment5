# Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.

# Input two numbers.
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

# If the first number and the second number has the same value print Equal.
if num1 == num2:
    print("Equal.")

# Or else print the max number.
else:
    print(f"The bigger number is {max(num1, num2)}.")