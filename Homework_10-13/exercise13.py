'''
    Գրեք ֆունկցիա, որը կստանա երկու ամբողջ թիվ ու 
    կտպի թե այդ թվերից որն է մեծ, որը՝ փոքր, կամ՝ հավասար։
    Ֆունցիան չպետք է օգտագործի համեմատության օպերատորներ։
'''

def input_number():
    while True:
        num = input("Enter a number: ")
        if num.isdigit():
            return int(num)
        print("Invalid input! Please enter a number:")

def compare_numbers(a, b):
    if a == b:
        print(f"{a} is equal to {b}")
    elif a > b:
        print(f"{a} is greater than {b}")
    else:
        print(f"{a} is less than {b}")


num1 = input_number("Enter the first number: ")
num2 = input_number("Enter the second number: ")


compare_numbers(num1, num2)

