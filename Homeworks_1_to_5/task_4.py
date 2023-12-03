'''
    Print the following pattern
    1
    2 2
    3 3 3
    4 4 4 4
    5 5 5 5 5
'''

rows = input('Enter the count of rows: ')

while True:
    if rows.isdigit():
        rows = int(rows)
        break
    else:
        rows = input('The count of rows must be an integer: ')

for i in range(1, rows + 1):
    print((str(i) + ' ') * i)