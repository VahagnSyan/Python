# Print the following pattern
# 1
# 2 2
# 3 3 3


def print_pattern(n):
    try:
        n = int(n)
    except ValueError:
        return print("Error: Please enter a valid integer for the number ")

    for i in range(1, n + 1):
        print((str(i) + " ") * i)


n = input("Enter  number : ")
print_pattern(n)
