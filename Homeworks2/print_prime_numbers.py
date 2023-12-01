"""
    Գրեք այնպիսի ֆունկցիա, որը ստանում է  ամբողջ թիվ և տպում այդ թվից փոքր
    կամ հավասար բոլոր պարզ թվերը: Պարզ թիվը 1-ից մեծ դրական ամբողջ թիվ է,
    որը բաժանվում է միայն իր և 1-ի վրա:
"""


def input_number():
    number = int(input("Enter the number: "))
    while number <= 1:
        number = int(input("Please enter number bigger than 1: "))
    return number


def print_prime_numbers(number):
    for i in range(1, number + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)


number = input_number()
print(print_prime_numbers(number))
