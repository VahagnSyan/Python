'''
The program prints pattern by inputed rows like:
1
2 2
3 3 3
'''


n = int(input("Enter the number of rows: ")) # input the number of rows
for i in range(1, n + 1):
    print(i * f"{i} ")
