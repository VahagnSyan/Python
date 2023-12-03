'''
Initializing matrix with given m and n
'''
import random   #library  for generating random numbers

Rows=int(input("enter the number of rows:\n"))
Column=int(input("enter the number of  columns:\n"))
m=Rows
n=Column
matrix =[]
for row in range(m):
    a=[]
    for column in range(n):
        a.append(random.randrange(0,9))
    matrix.append(a)

for row in range(m):
    for column in range(n):
        print(matrix[row][column], end=' ')
    print()

