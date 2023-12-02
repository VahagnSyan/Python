'''
    Գրեք ֆունկցիա, որը կստանա երկու ամբողջ թիվ ու 
    կտպի թե այդ թվերից որն է մեծ, որը՝ փոքր, կամ՝ հավասար։
    Ֆունցիան չպետք է օգտագործի համեմատության օպերատորներ։
'''

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

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

compare_numbers(num1, num2)
