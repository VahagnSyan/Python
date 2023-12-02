'''
    Գրեք ֆունկցիա, որը ստեղծում է ամբողջ թվերի մատրիցա։
    Մուտքագրվում է երկու m և n թվեր և ստեղծում է m x n 
    չափի մատրիցա, որը լցված է 0-ից 9-ի միջև պատահական ամբողջ թվերով:

'''

import random

def input_matrix_size():
    m = int(input("Enter the count of rows: "))
    while m < 1:
        m = int(input("Row size of matrix should be bigger than 0: "))

    n = int(input("Enter the count of columns: "))
    while n < 1:
        n = int(input("Column size of matrix should be bigger than 0: "))

    return m, n

def matrix(m, n):
    #generates 'm' rows to form the matrix
    return [[random.randint(0, 9) for _ in range(n)] for _ in range(m)] 

m, n = input_matrix_size()
print(matrix(m, n))
