# Input two numbers.
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

# If the 1st number is not equal to 2nd number, print not equal.
if num1 != num2:
    print("Not equal.")

# Else, print the smaller number between two numbers.
else:
    print(f"The smaller number is {min(num1, num2)}.")