# Գրեք այնպիսի ֆունկցիա, որը ստանում է  ամբողջ թիվ
# և տպում այդ թվից փոքր կամ հավասար բոլոր պարզ թվերը:
# Պարզ թիվը 1-ից մեծ դրական ամբողջ թիվ է, որը բաժանվում է միայն իր և 1-ի վրա:


def is_prime_number(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


try:
    number = int(input("Enter Number :"))
    print(is_prime_number(number))
except ValueError:
    print("Error: Please enter a valid integer for the number ")
