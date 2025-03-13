# Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

# Output: All the numbers from 1-100 except numbers ending in zero.
print("All numbers from 1-100 that doesn't end with zeros: ")

# Determine the numbers ending with zero, and exclude them.
for num in range(0, 100):
    if num % 10 != 0:

# Print the included numbers.
        print(num)
