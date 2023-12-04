'''

Prints prime numbers up to n

'''

def get_valid_int_input():
    valid_input = False
    while not valid_input:
        user_input = input("Input the number: ")
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input. Please enter a valid integer.")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes(n):
    for i in range(2, n + 1):
        if is_prime(i):
            print(i)


num = get_valid_int_input()
print_primes(num)

