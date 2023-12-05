# Գրեք ֆունկցիա, որը ստեղծում է ամբողջ թվերի մատրիցա։
# Մուտքագրվում է երկու m և n թվեր և ստեղծում է m x n չափի մատրիցա,
# որը լցված է 0-ից 9-ի միջև պատահական ամբողջ թվերով:


from random import randint
from os import system
from time import sleep

try:
    Row = int(input("Enter the number of rows:"))
    Column = int(input("Enter the number of columns:"))

    matrix = []

    for row in range(Row):
        a = []

        for column in range(Column):
            a.append(randint(0, 100))
        matrix.append(a)

    for row in range(Row):
        for column in range(Column):
            print(matrix[row][column], end=" ")
        print()

except:
    print("Error: Please enter a valid integer for the number ")
    sleep(2)
    system("clear")
    system("python3 ex_11.py")
