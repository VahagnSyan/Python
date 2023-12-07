'''
Գրեք այնպիսի ֆունկցիա, որը ստանում է  ամբողջ թիվ և տպում այդ թվից փոքր կամ հավասար բոլոր պարզ թվերը:
Պարզ թիվը 1-ից մեծ դրական ամբողջ թիվ է, որը բաժանվում է միայն իր և 1-ի վրա:
'''

def is_simple(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_simple_numbers(n):
    for i in range(2, n + 1):
        if is_simple(i):
            print(i)

while True:
    user_input = input("Enter a number: ")
    if user_input.isdigit():
        num = int(user_input)
        if num > 0:
            print(f"Prime numbers less than or equal to {num}:")
            print_simple_numbers(num)
            break
        else:
            print("Please enter a positive integer.")
    else:
        print("Invalid input. Please enter a valid number.")
