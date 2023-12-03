'''
Գրեք ֆունկցիա, որը ստեղծում է ամբողջ թվերի մատրիցա։
Մուտքագրվում է երկու m և n թվեր և ստեղծում է m x n չափի մատրիցա, 
որը լցված է 0-ից 9-ի միջև պատահական ամբողջ թվերով:
'''


import random

def create_random_matrix(row, column):
    matrix = []
    for i in range(row):
        matrix.append([])
        for _ in range(column):
            matrix[i].append(random.randint(0, 9))

    return matrix

row = int(input('Enter count of rows: '))
column = int(input('Enter count of columns: '))

result_matrix = create_random_matrix(row, column)

for row in result_matrix:
    print(row)
