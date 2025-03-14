# Input a number.
highest_number = None

while True:
    try:
        num = int(input("Enter a number: "))

# Determine the highest number.
        if highest_number is None or num > highest_number:
            highest_number = num

# Print the highest number.
    except ValueError:
        if highest_number is not None:
            print(f"The highest number is {highest_number}.")
        else:
            print("No valid numbers are inputted.")
        break