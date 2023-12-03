"""
    ex.4
    Print the following pattern
    1 
    2 2 
    3 3 3 
"""


rows = int(input("rows = "))

for i in range(1, rows + 1):
    print((str(i) + " ") * i)

