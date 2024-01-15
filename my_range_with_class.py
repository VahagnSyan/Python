class MyRange:
    def __init__(self, *args):
        if not args:
            raise ValueError("You didn't insert any arguments.")
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
        return self

    def __next__(self):
        if (self.start < self.end and self.step > 0) or \
              (self.start > self.end and self.step < 0):
            result = self.start
            self.start += self.step
            return result
        else:
            raise StopIteration

    def __eq__(self, other):
        return list(self) == other


assert list(MyRange(5)) == [0, 1, 2, 3, 4]
assert list(MyRange(1, 5)) == [1, 2, 3, 4]
assert list(MyRange(1, 10, 2)) == [1, 3, 5, 7, 9]
assert list(MyRange(10, 1, -1)) == [10, 9, 8, 7, 6, 5, 4, 3, 2]
assert list(MyRange(10, 1, 1)) == []
assert list(MyRange(3, 30, 3)) == [3, 6, 9, 12, 15, 18, 21, 24, 27]
print("All assertions passed!")
