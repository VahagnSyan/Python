"""
Գրեք ֆունկցիա, որը ստեղծում է ամբողջ թվերի մատրիցա։
Մուտքագրվում է երկու m և n թվեր և ստեղծում է m x n չափի մատրիցա, 
որը լցված է 0-ից 9-ի միջև պատահական ամբողջ թվերով:
"""


import random

def matrix_addition(row, column):  # Return the matrix with random numbers
    result_matrix = []
    for i in range(row):
        result_matrix.append([])  
        for _ in range(column):
            result_matrix[i].append(random.randint(0, 9))
    
    return result_matrix

matrix_row = input("Enter the number of rows: ")
while not matrix_row.isdigit():
    matrix_row = input("Enter the number of rows: ")

matrix_column = input("Enter the number of columns: ")
while not matrix_column.isdigit():
    matrix_column = input("Enter the number of columns: ")

matrix = matrix_addition(int(matrix_row), int(matrix_column))
print(matrix)