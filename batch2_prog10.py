#Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

# Input two numbers.
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

# Determine the numbers between two inputted two numbers.
number_step = 1 if num1 < num2 else -1
for num in range(num1 + number_step, num2, number_step):

# Print the determined numbers.