# Input a number.
num_list = []

while True:
    try:
        num = int(input("Enter a number: "))
        num_list.append(num)

# Determine numbers from highest to lowest and print.
    except ValueError:
        if num_list:
            num_list.sort(reverse=True)
            print(f"The numbers from highest to lowest are: {num_list}")
        else:
            print("No valid entry inputted.")
        break