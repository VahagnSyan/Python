""" ex11.py
    Գրեք ֆունկցիա, որը ստեղծում է ամբողջ թվերի մատրիցա։
    Մուտքագրվում է երկու m և n թվեր և ստեղծում է m x n չափի մատրիցա,
    որը լցված է 0-ից 9-ի միջև պատահական ամբողջ թվերով:
"""

import random

def input_number(symbol):
    num = input(f"Input {symbol}: ")
    while True:
        if num.isdigit():
            return int(num)
        else:
            num = input("Input again: ")

# make an M x N matrix and fill it with random numbers from 0 to 9
def make_matrix(m, n):
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(random.choice(range(10)))
        matrix.append(row)
    return matrix

matrix = make_matrix(input_number("m"), input_number("n"))
for i in matrix:
    print(i)

