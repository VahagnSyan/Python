'''
Գրեք ֆունկցիա, որը ստեղծում է ամբողջ թվերի մատրիցա։
Մուտքագրվում է երկու m և n թվեր և ստեղծում է m x n չափի մատրիցա, որը լցված է 0-ից 9-ի միջև պատահական ամբողջ թվերով:
'''

import random

def random_matrix(Row, Column):
    for row in range(Row): 
        a = []
        for column in range(Column): 
            a.append(random.randint(1, 9))
        matrix.append(a)

Row = int(input("Enter the number of rows:"))
Column = int(input("Enter the number of columns:"))

matrix = []
random_matrix(Row, Column)

for row in range(Row):
	for column in range(Column):
		print(matrix[row][column], end=" ")
	print()
