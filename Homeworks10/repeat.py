"""
    Implement repeat function from itertools.
"""


def repeat(obj, times=None):
    if times is None:
        while True:
            yield obj
    else:
        for i in range(times):
            yield obj


numbers = [1, 2, 3]

for item in repeat(numbers, 3):
    print(item)
