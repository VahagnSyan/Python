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


assert list(custom_map(square, [1, 2, 3, 4, 5])) == [1, 4, 9, 16, 25]
assert list(custom_map(square, [5, -1, 2, 8, 10])) == [25, 1, 4, 64, 100]
assert list(custom_map(square, [-3, 7, 0, -4, 100])) == [9, 49, 0, 16, 10000]
