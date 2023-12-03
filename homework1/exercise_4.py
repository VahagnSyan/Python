"""
    Print the following pattern
    1 
    2 2 
    3 3 3 
    4 4 4 4 
    5 5 5 5 5

"""
def get_valid_number():  # Check if the input number is valid
    while True:
        try:
            input_number = int(input("Enter the number: "))
            return input_number
        except ValueError:
            print("Invalid input. Please enter a valid number.")


quantity = get_valid_number()
for i in range(1, int(quantity)+1):
    for j in range(i):
        print(i, end = " ")
    print()