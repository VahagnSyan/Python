'''
    Գրեք այնպիսի ֆունկցիա, որը ստանում է  ամբողջ թիվ և
     տպում այդ թվից փոքր կամ հավասար բոլոր պարզ թվերը:

'''

def input_number():
    while True:
        num = input("Enter a number: ")
        if num.isdigit() and int(num) > 1:
            return int(num)
        print("Invalid input! Please enter a number:")

def is_prime(num):
    divider = 2
    while divider * divider <= num:
        if num % divider== 0:
            return False
        divider += 1
    return True

def print_prime_numbers(number):
    for i in range(2, number + 1):
        if is_prime(i):
            print(i)

number = input_number()
print_prime_numbers(number)

