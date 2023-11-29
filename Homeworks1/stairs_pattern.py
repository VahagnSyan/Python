"""
    Print the following pattern
    1 
    2 2 
    3 3 3 
    4 4 4 4 
    5 5 5 5 5
"""

input_size = 6 # Magic value

for i in range(1, input_size):
    for j in range(i):
        print(i, end=" ")
    print()