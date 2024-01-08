"""
    Implement map function of python.
"""


def square(num):
    """
    Gets number as argument and returns its square
    """

    return num**2


def custom_map(func, iterable):
    for i in iterable:
        yield func(i)


l = [1, 2, 3, 4, 5]


for i in custom_map(square, l):
    print(i)
