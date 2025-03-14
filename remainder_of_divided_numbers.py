# Input two numbers.
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

# If the 2nd number is equal to zero, output: not allowed.
if num2 == 0:
    print("Numbers divided by zero is undefined.")

# Print the remainder when the 1st number is divided by the 2nd number.
else:
    print(f"The remainder is {num1 % num2}.")