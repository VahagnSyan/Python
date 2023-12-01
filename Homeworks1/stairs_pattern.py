"""
    Print the following pattern
    1 
    2 2 
    3 3 3 
    4 4 4 4 
    5 5 5 5 5
"""


def input_size():
    size = int(input("Input the size of stairs pattern: "))
    return size


size = input_size()


for i in range(1, size):
    for j in range(i):
        print(i, end=" ")
    print()
