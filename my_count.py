class Сount:
    def __init__(self, *args):
        if not args:
            self.start, self.step = 0, 1
        elif len(args) > 2:
            raise ValueError("Too many arguments.")
        elif len(args) == 1:
            self.start, self.step = args[0], 1
        else:
            self.start, self.step = args
        self.current = self.start

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            result = self.current
            self.current += self.step
            return result 

    def __eq__(self, other):
        return list(self) == other


a = Сount(1, 2)
assert next(a) == 1
assert next(a) == 3
assert next(a) == 5
assert next(a) == 7