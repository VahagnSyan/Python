"""
Գրեք ֆունկցիա, որը կստանա երկու ամբողջ թիվ 
ու կտպի թե այդ թվերից որն է մեծ, որը՝ փոքր, կամ՝ հավասար։
Ֆունցիան չպետք է օգտագործի համեմատության օպերատորներ։
"""


def prime_nums(prime):
    for num in range(2, prime):
        if num > 1:
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0:
                    is_prime = False
                    break
            if is_prime:
                print(num)

input_num = input('Enter the number: ')
while not input_num.isdigit():
    input_num = input('Enter the number: ')


prime_nums(int(input_num))
