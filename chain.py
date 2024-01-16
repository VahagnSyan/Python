def chain(*iterables):
    for iterable in iterables:
        yield from iterable

l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']
l3 = (True, False)

print(list(chain(l1, l2, l3)))

# Test case 2: Empty iterables
result = list(chain([], [], ()))
assert result == [], f"Test case 2 failed: {result}"

# Test case 3: Strings
s1 = 'abc'
s2 = '123'
result = list(chain(s1, s2))
assert result == ['a', 'b', 'c', '1', '2', '3'], f"Test case 3 failed: {result}"

print("All test cases passed!")
