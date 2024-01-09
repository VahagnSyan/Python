from operator import add

def map_yield(func, iterable1, iterable2):
    for val1, val2 in zip(iterable1, iterable2):
        yield func(val1, val2)

# Example usage
l1 = [1, 2, 3, 7, 8]
l2 = [4, 5, 6]

result_iterator = map_yield(add, l1, l2)

for value in result_iterator:
    print(value)

print(type(map_yield(add, l1, l2)))  # Output: <class 'generator'>

