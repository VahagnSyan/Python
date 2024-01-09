"""
    Implement range function of python.
"""


def custom_range(start, end=None, step=1):
    if end is None:
        end = start
        start = 0

    if step > 0:
        while start < end:
            yield start
            start += step
    else:
        while start > end:
            yield start
            start += step


assert list(custom_range(5)) == [0, 1, 2, 3, 4]
assert list(custom_range(10, 0, -1)) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
assert list(custom_range(2, 8, 2)) == [2, 4, 6]
