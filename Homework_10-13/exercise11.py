'''
    Գրեք ֆունկցիա, որը ստեղծում է ամբողջ թվերի մատրիցա։
    Մուտքագրվում է երկու m և n թվեր և ստեղծում է m x n 
    չափի մատրիցա, որը լցված է 0-ից 9-ի միջև պատահական ամբողջ թվերով:

'''

import random

def input_number(prompt):
    while True:
        num = input(prompt)
        if num.isdigit() and int(num) > 0:
            return int(num)
        print("Invalid input! Please enter a number greater than 0.")

def input_matrix_size():
    m = input_number("Enter the count of rows: ")
    n = input_number("Enter the count of columns: ")
    return m, n

def matrix(m, n):
    # generates 'm' rows and 'n' columns for the matrix
    return [[random.randint(0, 9) for _ in range(n)] for _ in range(m)]

m, n = input_matrix_size()
print(matrix(m, n))


