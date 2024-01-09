"""
    Implement filter function of python.
"""


def is_even(num):
    return num % 2 == 0


def custom_filter(func, iterable):
    for item in iterable:
        if func(item):
            yield item


assert list(custom_filter(is_even, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == [2, 4, 6, 8, 10]
assert list(custom_filter(is_even, [1, 1, 1])) == []
assert list(custom_filter(is_even, [-5, 4, -4])) == [4, -4]
