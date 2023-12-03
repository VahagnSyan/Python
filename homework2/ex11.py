"""
    Գրեք ֆունկցիա, որը ստեղծում է ամբողջ թվերի մատրիցա։
    Մուտքագրվում է երկու m և n թվեր և ստեղծում է m x n չափի մատրիցա, որը լցված է 0-ից 9-ի միջև պատահական ամբողջ թվերով:

"""

from random import random

def create_matrix(num1, num2):
    matrix = []

    for i in range(num1):
        matrix.append([]) 
        for j in range(num2):
            value = random() * 10
            matrix[i].append(int(value))
    
    print(matrix)


def get_valid_number():  # Check if the input number is valid
    while True:
        try:
            input_number = int(input("Enter the number: "))
            return input_number
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    input_number1 = get_valid_number()
    input_number2 = get_valid_number()
    create_matrix(int(input_number1), int(input_number2))


main()
