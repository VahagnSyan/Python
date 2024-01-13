"""
    Implement accumulate function from itertools   
"""


from operator import add, mul


def accumulate(iterable, func=add):
    iterator = iter(iterable)

    try:
        sum = next(iterator)
    except StopIteration:
        return
    yield sum
    for item in iterator:
        sum = func(sum, item)
        yield sum


numbers = [1, 2, 3, 4, 5]
result = list(accumulate(numbers))
assert result == [1, 3, 6, 10, 15]

numbers = [1, 2, 3, 4, 5]
result = list(accumulate(numbers, mul))
assert result == [1, 2, 6, 24, 120]

empty_list = []
result = list(accumulate(empty_list))
assert result == []

one_element_list = [7]
result = list(accumulate(one_element_list))
assert result == [7]
