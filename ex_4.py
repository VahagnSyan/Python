'''
Print the following pattern
1
2 2
3 3 3
'''


def print_pattern(num):
    num = int(num)
    for i in range(1, num + 1):
        print((str(i) + " ") * i)


num = input("Enter  number : ")
while not num.isdigit():
    num = input("Enter  number : ")
print_pattern(num)
