"""
Գրեք ֆունկցիա, որը ստեղծում է ամբողջ թվերի մատրիցա։
Մուտքագրվում է երկու m և n թվեր և ստեղծում է m x n չափի մատրիցա, 
որը լցված է 0-ից 9-ի միջև պատահական ամբողջ թվերով:
"""


import random

def get_valid_number():  # Check if the input number is valid
    while True:
        try:
            input_number = int(input("Enter the number: "))
            return input_number
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
def matrix_addition(row, column):  # Return the matrix with random numbers
    result_matrix = []
    for i in range(row):
        result_matrix.append([])  
        for _ in range(column):
            result_matrix[i].append(random.randint(0, 9))
    
    return result_matrix

print("Enter the number of rows: ")
matrix_row = get_valid_number()

print("Enter the number of columns: ")
matrix_column = get_valid_number()

matrix = matrix_addition(matrix_row, matrix_column)
print(matrix)