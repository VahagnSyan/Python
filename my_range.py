def my_range(start, end=None, step=1):
    if end == None:
        end = start
        start = 0
    while start > end:
        yield start
        start -= step
    while start < end:
        yield start
        start += step


assert list(my_range(5)) == [0, 1, 2, 3, 4]

assert list(my_range(2, 8, 2)) == [2, 4, 6]

assert list(my_range(10, 5)) == [10, 9, 8, 7, 6]

assert list(my_range(5, 5)) == []

assert list(my_range(0, 10, 3)) == [0, 3, 6, 9]

assert list(my_range(10, 0)) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

assert list(my_range(5, 2)) == [5, 4, 3]

assert list(my_range(3, 3)) == []

assert list(my_range(0, -5)) == [0, -1, -2, -3, -4]

print("All assertions passed!")

