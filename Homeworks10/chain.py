"""
    Implement chain function from itertools.
"""


def chain(*iterables):
    for iterable in iterables:
        for item in iterable:
            yield item


numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
letters = ["a", "b", "c"]

result = list(chain(numbers1, numbers2, letters))
assert result == [1, 2, 3, 4, 5, 6, "a", "b", "c"]

empty_iterable = []
result = list(chain(empty_iterable, numbers1, letters))
assert result == [1, 2, 3, "a", "b", "c"]

result = list(chain())
assert result == []
