'''
    Ex.10
    Գրեք այնպիսի ֆունկցիա, որը ստանում է  ամբողջ թիվ
    և տպում այդ թվից փոքր կամ հավասար բոլոր պարզ թվերը:
    Պարզ թիվը 1-ից մեծ դրական ամբողջ թիվ է, որը բաժանվում է միայն իր և 1-ի վրա:
'''

def input_num():
    while True:
        num = input("Enter a number greater than 1: ")
        if num.isdigit() and int(num) > 1:
            return int(num)
        print("Invalid input! Please enter a number greater than 1.")

def prime_nums(candidate):
    divisor = 2
    while divisor * divisor <= candidate:
        if candidate % divisor == 0:
            return False
        divisor += 1
    return True

def print_prime_nums(num):
    for i in range(2, num + 1):
        if prime_nums(i):
            print(i)

num = input_num()
print_prime_nums(num)
