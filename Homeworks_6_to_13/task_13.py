'''
    Ex. 13
    Գրեք ֆունկցիա, որը կստանա երկու ամբողջ թիվ ու կտպի թե այդ թվերից որն է
    մեծ, որը՝ փոքր, կամ՝ հավասար։
    Ֆունցիան չպետք է օգտագործի համեմատության օպերատորներ։
'''
def compare_numbers(a, b):
    difference = a - b
    if difference == 0:
        print(f'{a} is equal to {b}')
    else:
        # Check the sign of the difference
        sign = difference // abs(difference)
        if sign == 1:
            print(f'{a} is greater than {b}')
        else:
            print(f'{a} is less than {b}')

def correct_input(num):
    while True:
        if num.isdigit():
            break
        num = input('The number must be an integer: ')

num1 = input('Enter the first number: ')
correct_input(num1)
num1 = int(num1)

num2 = input('Enter the second number: ')
correct_input(num2)
num2 = int(num2)

compare_numbers(num1, num2)
