# Output: All odd numbers from 1 to 100.
print("All odd numbers from 1-100: ")

# While less than a hundred and the remainder when divided by two is not equal to zero include the number.
num = 1
while num <= 100:
    if num % 2 != 0:

# Print all included numbers.
        print(num)
        num += 2