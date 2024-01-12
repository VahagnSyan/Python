class Accumulate:
    def __init__(self, *args):
        if not args:
            raise ValueError("You didn't insert any arguments.")
        elif len(args) > 2:
            raise ValueError("Too many arguments.")
        elif len(args) == 1:
            if not hasattr(args[0], '__iter__'):
                raise ValueError("The argument must be an iterable.")
            self.list = args[0]
            self.function = lambda num1, num2: num1 + num2
        else:
            if not hasattr(args[0], '__iter__'):
                raise ValueError("The first argument must be an iterable.")
            if not callable(args[1]):
                raise ValueError("The second argument must be a callable function.")
            self.list, self.function = args

    def __iter__(self):
        accum = self.list[0]
        yield accum
        for i in range(1, len(self.list)):
            accum = self.function(self.list[i], accum)
            yield accum


    def __eq__(self, other):
        return list(self) == other


def mul(num1, num2):
    return num1 * num2


assert list(Accumulate([1, 2, 3, 10, 32])) == [1, 3, 6, 16, 48]
assert list(Accumulate([1, 2, 3, 10, 32], mul)) == [1, 2, 6, 60,1920]
print("All assertions passed!")
