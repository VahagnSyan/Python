"""
Գրեք ֆունկցիա, որը ստեղծում է ամբողջ թվերի մատրիցա։
Մուտքագրվում է երկու m և n թվեր և ստեղծում է m x n չափի մատրիցա, 
որը լցված է 0-ից 9-ի միջև պատահական ամբողջ թվերով:
"""


import random

def matrix_addition(row, column):  # Return the matrix with random numbers
    result_matrix = []
    for _ in range(row):
        middle_matrix = []  # Generate a middle matrix with random numbers
        for _ in range(column):
            middle_matrix.append(random.randint(1, 9))
        
        result_matrix.append(middle_matrix)
    
    return result_matrix

def print_matrix(matrix):  # Print the 2 dimensional matrix elements
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()

matrix_row = input("Enter the number of rows: ")
while not matrix_row.isdigit():
    matrix_row = input("Enter the number of rows: ")

matrix_column = input("Enter the number of columns: ")
while not matrix_column.isdigit():
    matrix_column = input("Enter the number of columns: ")

matrix = matrix_addition(int(matrix_row), int(matrix_column))
print_matrix(matrix)