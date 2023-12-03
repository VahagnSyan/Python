'''
    Գրեք ֆունկցիա, որը կստանա երկու ամբողջ թիվ ու 
    կտպի թե այդ թվերից որն է մեծ, որը՝ փոքր, կամ՝ հավասար։
    Ֆունցիան չպետք է օգտագործի համեմատության օպերատորներ։
'''
def input_number():
    while True:
        num = input()
        if num.isdigit():
            return int(num)
        print("Invalid input! Please enter a number:")

print("Enter the first number: ")
num1 = input_number()
print("Enter the second number: ")
num2 = input_number()

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
