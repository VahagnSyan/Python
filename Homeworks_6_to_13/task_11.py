'''
    Գրեք ֆունկցիա, որը ստեղծում է ամբողջ թվերի մատրիցա։
    Մուտքագրվում է երկու m և n թվեր և ստեղծում է m x n 
    չափի մատրիցա, որը լցված է 0-ից 9-ի միջև պատահական ամբողջ թվերով:

'''

import random

def input_matrix_size():
    while True:
        m = input('Enter the count of rows: ')
        if m.isdigit() and int(m) >= 1:
            m = int(m)
            break
        print("Invalid input! The count of rows should be greater than or equal to 1.")

    while True:
        n = input('Enter the count of columns: ')
        if n.isdigit() and int(n) >= 1:
            n = int(n)
            break
        print("Invalid input! The count of columns should be greater than or equal to 1.")

    return m, n

def generate_matrix(m, n):
    return [[random.randint(0, 9) for _ in range(n)] for _ in range(m)] 

m, n = input_matrix_size()
print(generate_matrix(m, n))