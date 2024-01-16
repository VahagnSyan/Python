class MyRange:
    def __init__(self, *args):
        args_count = len(args)
        if args_count == 0 or args_count >= 4:
            raise AttributeError('Expected 1, 2, or 3 arguments')

        self.step = 1

        if args_count == 1:
            self.stop, = args
            self.start = 0
        elif args_count == 2:
            self.start, self.stop = args
        else:
            self.start, self.stop, self.step = args
            if self.step == 0:
                raise ValueError('Step cannot be zero')

        self._current = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if (self.step > 0 and self._current < self.stop) or (self.step < 0 and self._current > self.stop):
            result = self._current
            self._current += self.step
            return result
        raise StopIteration

# Test case 1: Custom start, stop, and step
my_range = MyRange(2, 10, 2)
assert list(my_range) == [2, 4, 6, 8], f"Test case 1 failed: {list(my_range)}"
assert list(my_range) == [], "Repeated iteration should result in an empty list"

# Test case 2: Custom start and stop with default step
my_range = MyRange(5)
assert list(my_range) == [0, 1, 2, 3, 4], f"Test case 2 failed: {list(my_range)}"
assert list(my_range) == [], "Repeated iteration should result in an empty list"

# Test case 3: Custom start, stop, and negative step
my_range = MyRange(10, 2, -2)
assert list(my_range) == [10, 8, 6, 4], f"Test case 3 failed: {list(my_range)}"
assert list(my_range) == [], "Repeated iteration should result in an empty list"

# Test case 4: Custom start, stop, and step with zero step (should raise ValueError)
try:
    my_range = MyRange(1, 10, 0)
    assert False, "Expected ValueError for zero step, but no exception was raised"
except ValueError:
    pass  # Expected behavior

# Test case 5: Too many arguments (should raise AttributeError)
try:
    my_range = MyRange(1, 10, 2, 5)
    assert False, "Expected AttributeError for too many arguments, but no exception was raised"
except AttributeError:
    pass  # Expected behavior

print("All assertions passed!")
