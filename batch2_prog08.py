# Prog08: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)

# Output: All odd numbers from 1 to 100.
print("All odd numbers from 1-100: ")

# While less than a hundred and the remainder when divided by two is not equal to zero include the number.
num = 1
while num <= 100:
    if num % 2 != 0:

# Print all included numbers.
        print(num)
        num += 2