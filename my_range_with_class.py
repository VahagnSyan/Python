class MyRange:
    def __init__(self, *args):
        if not args:
            raise ValueError("You dont insert any arguments.")
        elif len(args) > 3:
            raise ValueError("Too many arguments.")
        elif len(args) == 1:
            self.end = args[0]
            self.start = 0
            self.step = 1
        elif len(args) == 2:
            self.start, self.end = args
            self.step = 1
        else:
            self.start, self.end, self.step = args

    def __iter__(self):
        while (self.start < self.end and self.step > 0) or \
              (self.start > self.end and self.step < 0):
            yield self.start
            self.start += self.step

    def __eq__(self, other):
        return list(self) == other


assert MyRange(5) == [0, 1, 2, 3, 4]
assert MyRange(2, 8, 2) == [2, 4, 6]
assert MyRange(10, 5) == []
assert MyRange(5, 5) == []
assert MyRange(0, 10, 3) == [0, 3, 6, 9]
assert MyRange(10, 5, -1) == [10, 9, 8, 7, 6]
assert MyRange(5, 2, -2) == [5, 3]
assert MyRange(3, 3) == []
assert MyRange(0, 5, -1) == []
print("All assertions passed!")

