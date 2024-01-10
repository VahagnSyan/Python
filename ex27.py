'''
Accumulate function
'''

def accumulate(iterable, func=lambda x, y: x + y):
    it = iter(iterable)
    total = next(it)
    yield total
    for element in it:
        total = func(total, element)
        yield total

numbers = [1, 2, 3, 4, 5]
result = list(accumulate(numbers))
print(result)
