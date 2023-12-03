'''Գրեք ֆունկցիա, որը կստանա երկու ամբողջ թիվ ու կտպի 
թե այդ թվերից որն է մեծ, որը՝ փոքր, կամ՝ հավասար։
Ֆունցիան չպետք է օգտագործի համեմատության օպերատորներ։
'''


def compare_nums(num1, num2):
    if not(num1 - num2):
        print(f"{num1} = {num2}")
    elif not(num2) and num1 + abs(num1):
        print(f"{num1} > {num2}")
    elif not(num2) and not(num1 + abs(num1)):
        print(f"{num1} < {num2}")
    elif not(num1) and not(num2 + abs(num2)):
        print(f"{num1} > {num2}")
    elif not(num1 + abs(num1)):
        if not(num2 + abs(num2)) and not(num1 // num2):
            print(f"{num1} > {num2}")
        elif not(num2 + abs(num2)) and num1 // num2:
            print(f"{num1} < {num2}")
        else:
            print(f"{num1} < {num2}")
    elif num1 // num2:
        print(f"{num1} > {num2}")
    else:
        print(f"{num1} < {num2}")
        
input_num1 = int(input("Enter the first number: "))
input_num2 = int(input("Enter the second number: "))
compare_nums(input_num1, input_num2) 
