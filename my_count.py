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

    def __iter__(self):
        while True:
            yield self.start
            self.start += self.step

    def __eq__(self, other):
        return list(self) == other
