"""
Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5

"""

quantity = int(input("Enter quantity of rows: "))

for i in range(1, quantity+1):
    for j in range(i):
        print(i, end = " ")
    print()