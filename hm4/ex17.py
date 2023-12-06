"""
    try to guess the random number
"""

from random import randint


def get_valid_number():  # Check if the input number is valid
    while True:
        try:
            input_number = int(input("Enter the number: "))
            return input_number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    target = randint(1, 100)

    while True:
        input_num = get_valid_number()
        if(input_num == target):
            print("You won")
            break
        elif(input_num > target):
            print("the entered number is larger: ")
        else:
            print("the entered number is smaller")


main()