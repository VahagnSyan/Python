"""
    Print the following pattern
    1 
    2 2 
    3 3 3 
    4 4 4 4 
    5 5 5 5 5

"""

quantity = input("Enter quantity of rows: ")
while not quantity.isdigit():
    quantity = input("Enter the number: ")

for i in range(1, int(quantity)+1):
    for j in range(i):
        print(i, end = " ")
    print()