'''
Գրեք ֆունկցիա, որը ստեղծում է ամբողջ թվերի մատրիցա։
Մուտքագրվում է երկու m և n թվեր և ստեղծում է m x n չափի մատրիցա, որը լցված է 0-ից 9-ի միջև պատահական ամբողջ թվերով:
'''

import random

def mn_matrix(m, n):
    matrix = [[random.randint(0, 9) for _ in range(n)] for _ in range(m)]
    return matrix

while True:
    m_input = input("Enter number of columns: ")
    if m_input.isdigit():
        m = int(m_input)
        if m > 0:
            n_input = input("Enter number of rows: ")
            if n_input.isdigit():
                n = int(n_input)
                if n > 0:
                    result = mn_matrix(m, n)
                    for row in result:
                        print(row)
                    break  
                else:
                    print("Please enter a positive integer.")
            else:
                print("Invalid input. Please enter a valid number.")
        else:
            print("Please enter a positive integer.")
    else:
        print("Invalid input. Please enter a valid number.")
