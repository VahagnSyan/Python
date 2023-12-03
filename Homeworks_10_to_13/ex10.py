""" ex10.py

	Գրեք այնպիսի ֆունկցիա, որը ստանում է  ամբողջ թիվ և տպում այդ թվից փոքր կամ հավասար բոլոր պարզ թվերը:
	Պարզ թիվը 1-ից մեծ դրական ամբողջ թիվ է, որը բաժանվում է միայն իր և 1-ի վրա:
"""

def is_prime(num):
    # Check if a number is prime.
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_before_n(n):
    if n < 2:
        print("No prime numbers.")
    else:
        print("Prime numbers up to", n, ":", end = ' ')
        for i in range(2, n):
            if is_prime(i):
                print(i, end=' ')
        print()

print_primes_before_n(20)

