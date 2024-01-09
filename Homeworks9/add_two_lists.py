"""
    Add two lists using custom map function.
"""


def custom_map(func, *iterables):
    iterators = [iter(iterable) for iterable in iterables]

    while True:
        try:
            yield func(*[next(iterator) for iterator in iterators])
        except StopIteration:
            break


list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4]
list3 = [2, 3, 4, 5]
list4 = [2, 3, 4, 5]
list5 = [2, 3, 4, 5]


def add(*args):
    return sum(args)


def multiplication(*args):
    result = 1
    for arg in args:
        result *= arg
    return result


result_add = custom_map(add, list1, list2, list3, list4, list5)
result_multiply = custom_map(multiplication, list1, list2, list3, list4, list5)

print("Addition:")
for num in result_add:
    print(num)

print("\nMultiplication:")
for num in result_multiply:
    print(num)
