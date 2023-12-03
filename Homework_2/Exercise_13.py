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
    # Check if numbers are equal
    if not(first_number-second_number):
        print(f"{first_number} = {second_number}")
    # Check if second number is 0
    elif not(second_number):  
        # Check if first number is less than 0
        if not(first_number + abs(first_number)): 
            print(f"{first_number} < {second_number}")
        else:
            print(f"{first_number} > {second_number}")
    # Check if first number is less than 0
    elif not(first_number + abs(first_number)):  
        # Check if both numbers are negative and first_number has the second_number
        if not(second_number + abs(second_number)) and first_number//second_number:
            print(f"{first_number} < {second_number}")
        # Check if both numbers are negative and first_number doesn't have the second_number
        elif not(second_number + abs(second_number)) and not(first_number//second_number):
            print(f"{first_number} > {second_number}")
        else:
            print(f"{first_number} < {second_number}")
    # Check if first_number has the second_number
    elif first_number//second_number:  
        print(f"{first_number} > {second_number}")
    else:
        print(f"{first_number} < {second_number}")

print("Now enter the first number!")
first_number = get_valid_number()

print("Now enter the second number!")
second_number = get_valid_number()

compare_numbers(first_number, second_number)