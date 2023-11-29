def compare_numbers(num1, num2):
    difference = num1 - num2
    sign = (difference > 0) - (difference < 0)

    if sign == 1:
        print(f"{num1} is greater than {num2}")
    elif sign == 0:
        print(f"{num1} is equal to {num2}")
    else:
        print(f"{num2} is greater than {num1}")

while True:  # infinite loop untill user input is valid
    try:     # trying to catch exceptions
        num1 = int(input("Enter the first integer: "))
        num2 = int(input("Enter the second integer: "))
        break            # if user input valid number -> break
    except ValueError:   # this line is responsible for catching exceptions
        print("Invalid input. Please enter a valid integer.")   # if exception was caught write
                                                                # helping msg to user
compare_numbers(num1, num2)
