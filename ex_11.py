'''
Գրեք ֆունկցիա, որը ստեղծում է ամբողջ թվերի մատրիցա։
Մուտքագրվում է երկու m և n թվեր և ստեղծում է m x n չափի մատրիցա,
որը լցված է 0-ից 9-ի միջև պատահական ամբողջ թվերով:
'''


from random import randint


row = input("Enter the number of rows:")
while not row.isdigit():
    num = input("Enter the number of rows: ")

column = input("Enter the number of columns: ")
while not column.isdigit():
    num = input("Enter the number of columns: ")

row = int(row) 
column = int(column)

matrix = []

for r in range(row):
    a = []
    for c in range(column):
        a.append(randint(0, 9))
    matrix.append(a)

for r in range(row):
    for c in range(column):
        print(matrix[r][c], end=" ")
    print()    



 
