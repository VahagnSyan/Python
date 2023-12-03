def max_of_two_numbers(num1, num2):
    return int((abs(num1 - num2) + num1 + num2) / 2)
while True:  # infinite loop untill user input is valid
    try:     # trying to catch exceptions
        num1 = int(input("Enter the first integer: "))
        num2 = int(input("Enter the second integer: "))
        break            # if user input valid number -> break
    except ValueError:   # this line is responsible for catching exceptions
        print("Invalid input. Please enter a valid integer.")   # if exception was caught write
                                                                # helping msg to user
result = max_of_two_numbers(num1, num2)
print("The Max number is:", result)
