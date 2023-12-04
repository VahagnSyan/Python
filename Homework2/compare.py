'''Գրեք ֆունկցիա, որը կստանա երկու ամբողջ թիվ ու կտպի 
թե այդ թվերից որն է մեծ, որը՝ փոքր, կամ՝ հավասար։
Ֆունցիան չպետք է օգտագործի համեմատության օպերատորներ։
'''


def find_max(num1, num2):
    difference = num1 - num2
    if difference == 0:
        print('numbers are equal')
        return

    sign = (difference >> 31) & 1 
    print(num1, num2, sep=' < ') if sign else print(num1, num2, sep=' > ')


def get_valid_number():
    while True:
        try:
            input_number = int(input("Enter the number: "))
            return input_number
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    input_number1 = get_valid_number()
    input_number2 = get_valid_number()
    find_max(int(input_number1), int(input_number2))


main()
