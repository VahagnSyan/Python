"""
    Ex.10
    Գրեք այնպիսի ֆունկցիա, որը ստանում է  ամբողջ թիվ և տպում այդ թվից փոքր կամ
    հավասար բոլոր պարզ թվերը:
"""


def is_prime(received_num):
    if received_num <= 1:
        return False
    for i in range(2, received_num):
        if received_num % i == 0:
            return False
    return True

def print_prime(number):
    print(number)
    for i in range(2, number + 1):
        if is_prime(i):
            print(i)

num = int(input("Enter the number "))
print_prime(num)
