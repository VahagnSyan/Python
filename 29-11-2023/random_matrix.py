import random

def create_random_matrix(m, n):
    matrix = [[random.randint(0, 9) for i in range(n)] for i in range(m)]
    return matrix

while True:  # infinite loop untill user input is valid
    try:     # trying to catch exceptions
        m = int(input("Enter the number of rows (m): "))
        n = int(input("Enter the number of columns (n): "))
        random_matrix = create_random_matrix(m, n)
        break            # if user input valid number -> break
    except ValueError:   # this line is responsible for catching exceptions
        print("Invalid input. Enter a valid integer for rows and columns")  # if exception was caught write
                                                                            # helping msg to user
print("Random Matrix:")
for i in random_matrix:
    print(i)
