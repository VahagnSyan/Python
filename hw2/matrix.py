'''

craeates MxN matrix with random elements

'''


import random


def get_valid_int_input(promt):
    valid_input = False
    while not valid_input:
        user_input = input(promt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input. Please enter a valid integer.")

def create_random_matrix(m, n):
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(random.randint(0, 9))
        matrix.append(row)
    return matrix

m = get_valid_int_input("Enter the number of rows (m): ")
n = get_valid_int_input("Enter the number of columns (n): ")

random_matrix = create_random_matrix(m, n)
print(f"Random {m} x {n} matrix:")
for row in random_matrix:
    print(row)

