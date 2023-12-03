'''
    Գրեք ֆունկցիա, որը կստանա երկու ամբողջ թիվ ու 
    կտպի թե այդ թվերից որն է մեծ, որը՝ փոքր, կամ՝ հավասար։
    Ֆունցիան չպետք է օգտագործի համեմատության օպերատորներ։
'''
def input_num(prompt):
    while True:
        num = input(prompt)
        if num.isdigit() and int(num) > 1:
            return int(num)
        print("Invalid input! Please enter a number greater than 1:")

num1 = input_num("Enter the first number: ")
num2 = input_num("Enter the second number: ")

def compare_numbers(a, b):
    diff = a - b
    if diff == 0:
        print(f"{a} is equal to {b}")
    else:
        sign = diff // abs(diff)  # Determines the sign of the difference
        if sign == 1:
            print(f"{a} is greater than {b}")
        else:
            print(f"{a} is less than {b}")

compare_numbers(num1, num2)
