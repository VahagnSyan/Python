'''
Range with class
'''

class MyRange:
    def __init__(self, *args):
        args_count = len(args)
        if args_count == 0 or args_count > 4:
            error = f'Expected 1, 2 or 3'
            raise AttributeError(error)
        self.step = 1
        if args_count == 1:
            self.start = 0
            self.stop = args
        elif args_count == 2:
            self.start, self.stop = args
        else:
            self.start, self.stop, self.step = args
            if self.stop == 0:
                raise ValueError('')

        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        

# Test case 1
result = list(MyRange(2, 10, 2))
assert result == [2, 4, 6, 8], f"Test case 1 failed: {result}"

# Test case 2: Default parameters
result = list(MyRange(5))
assert result == [0, 1, 2, 3, 4], f"Test case 2 failed: {result}"

# Test case 3: Negative step
result = list(MyRange(10, 2, -2))
assert result == [10, 8, 6, 4], f"Test case 3 failed: {result}"

print("All test cases passed!")
