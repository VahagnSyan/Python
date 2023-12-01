"""
Գրեք ֆունկցիա, որը ստեղծում է ամբողջ թվերի մատրիցա։
Մուտքագրվում է երկու m և n թվեր և ստեղծում է m x n չափի մատրիցա,
որը լցված է 0-ից 9-ի միջև պատահական ամբողջ թվերով:
"""

import random


def input_matrix_size():
    m = int(input("Enter rows count of matrix: "))
    while m < 1:
        m = int(input("Row size of matrix should be bigger than 0: "))

    n = int(input("Enter columns count of matrix: "))
    while n < 1:
        n = int(input("Column size of matrix should be bigger than 0: "))

    return m, n


def generate_matrix(m, n):
    generated_matrix = []

    for i in range(0, m):
        row = []
        for j in range(0, n):
            row.append(random.randint(0, 9))
        generated_matrix.append(row)

    return generated_matrix


m, n = input_matrix_size()
print(generate_matrix(m, n))
