def count(start=0, step=1):
    current = start
    while True:
        yield current
        current += step

counter = count(5, 2)
for _ in range(5):
    print(next(counter))

# Test case 1
counter = count(5, 2)
result = [next(counter) for _ in range(5)]
assert result == [5, 7, 9, 11, 13], f"Test case 1 failed: {result}"

# Test case 2: Default parameters
counter = count()
result = [next(counter) for _ in range(5)]
assert result == [0, 1, 2, 3, 4], f"Test case 2 failed: {result}"

print("All test cases passed!")
