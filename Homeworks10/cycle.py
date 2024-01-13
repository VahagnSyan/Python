"""
    Implement cycle function from itertools.
"""


def cycle(iterable):
    iterator = iter(iterable)
    while True:
        try:
            yield next(iterator)
        except StopIteration:
            iterator = iter(iterable)


numbers = [1, 2, 3]
cycled_numbers = cycle(numbers)

for i in range(5):
    print(next(cycled_numbers))
