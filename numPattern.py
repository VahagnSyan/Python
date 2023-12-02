'''
ex.4
Print the following pattern
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''

num_rows = int(input("Input the number of rows: "))
for i in range(1, num_rows + 1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()

