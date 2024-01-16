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

# Test case 1: default addition function
numbers = [1, 2, 3, 4, 5]
result = list(accumulate(numbers))
assert result == [1, 3, 6, 10, 15], f"Test case 1 failed: {result}"

# Test case 2: multiplication function
numbers = [1, 2, 3, 4, 5]
result = list(accumulate(numbers, func=lambda x, y: x * y))
assert result == [1, 2, 6, 24, 120], f"Test case 2 failed: {result}"

# Test case 3: custom function (e.g., subtraction)
numbers = [10, 5, 2, 1]
result = list(accumulate(numbers, func=lambda x, y: x - y))
assert result == [10, 5, 3, 2], f"Test case 3 failed: {result}"

# Test case 4: strings concatenation
strings = ['a', 'b', 'c', 'd']
result = list(accumulate(strings, func=lambda x, y: x + y))
assert result == ['a', 'ab', 'abc', 'abcd'], f"Test case 4 failed: {result}"

print("All test cases passed!")
