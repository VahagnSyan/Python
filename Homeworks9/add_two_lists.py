"""
    Add two lists using custom map function.
"""


def custom_map(add_function, list1, list2):
    iterator1 = iter(list1)
    iterator2 = iter(list2)

    while True:
        try:
            yield add_function(next(iterator1), next(iterator2))
        except StopIteration:
            break


list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4]


def add_elements(x, y):
    return x + y


result = custom_map(add_elements, list1, list2)

for num in result:
    print(num)
