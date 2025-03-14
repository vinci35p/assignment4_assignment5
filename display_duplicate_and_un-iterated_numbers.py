# Input a number.
number = []

while True:
    try:
        num = int(input("Enter a number: "))

# Print if number is duplicate.
        if num in number:
            print("Duplicate.")

# Print if number is unique.
        else:
            print("Unique.")
            number.append(num)

# Print if number is invalid then end the program.
    except ValueError:
        print("Invalid entry, exiting.")