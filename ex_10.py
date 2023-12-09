'''
Գրեք այնպիսի ֆունկցիա, որը ստանում է  ամբողջ թիվ
և տպում այդ թվից փոքր կամ հավասար բոլոր պարզ թվերը:
Պարզ թիվը 1-ից մեծ դրական ամբողջ թիվ է, որը բաժանվում է միայն իր և 1-ի վրա:
'''


def is_prime_number(num):
    num = int(num)
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


num = input("Enter  number : ")
while not num.isdigit():
    num = input("Enter  number : ")
print(f"{is_prime_number(num) = }")

