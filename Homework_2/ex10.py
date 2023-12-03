'''
Գրեք այնպիսի ֆունկցիա, որը ստանում է  ամբողջ թիվ և տպում այդ թվից փոքր կամ հավասար բոլոր պարզ թվերը:
Պարզ թիվը 1-ից մեծ դրական ամբողջ թիվ է, որը բաժանվում է միայն իր և 1-ի վրա:
'''
def print_primes(number):
    def is_prime(num):
        if num < 1:
            return False
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                return False
        return True
    for num in range(2, number + 1):
        if is_prime(num):
            print(num, end=' ')


number = int(input("Enter the number :"))
print("Prime numbers up to", number, "are :")
print_primes(number)

