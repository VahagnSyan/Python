"""
Գրեք ֆունկցիա, որը կստանա երկու ամբողջ թիվ 
ու կտպի թե այդ թվերից որն է մեծ, որը՝ փոքր, կամ՝ հավասար։
Ֆունցիան չպետք է օգտագործի համեմատության օպերատորներ։
"""


def get_valid_number():  # Check if the input number is valid
    while True:
        try:
            input_number = int(input("Enter the number: "))
            return input_number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def compare_numbers(first_number, second_number):
    difference = first_number - second_number
    if difference == 0:
        print(first_number, second_number, sep=' = ')
        return

    sign = (difference >> 31) & 1  # Return the sign of difference
    if sign:  # If sign is 1, first number is bigger than second
        print(first_number, second_number, sep=' < ')
    else:  # Otherwise, the first number is less than the second
        print(first_number, second_number, sep=' > ')

print("Now enter the first number!")
first_number = get_valid_number()

print("Now enter the second number!")
second_number = get_valid_number()

compare_numbers(first_number, second_number)