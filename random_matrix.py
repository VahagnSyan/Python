"""
    Ex.11
    Գրեք ֆունկցիա, որը ստեղծում է ամբողջ թվերի մատրիցա։
    Մուտքագրվում է երկու m և n թվեր և ստեղծում է m x n չափի մատրիցա, որը
    լցված է 0-ից 9-ի միջև պատահական ամբողջ թվերով: 
"""


import random

def create_matrix(m, n):
    matrix = []
    for _ in range(m):
        row = []
        for _ in range(n):
            row.append(random.randint(0, 9))
        matrix.append(row)
    return matrix

m = int (input("Enter m "))
n = int (input("Enter n "))

result = create_matrix(m, n)
print("The matrix is ")
for row in result:
    print(row) 
