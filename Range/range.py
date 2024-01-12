'''
    class Range
'''

class Range:
    '''
    Return an generator that produces a sequence of integers from start
    (inclusive) to stop (exclusive) by step.  range(i, j)
    produces i, i+1, i+2, ..., j-1. start defaults to 0, and stop is omitted!
    range(4) produces 0, 1, 2, 3.These are exactly the valid indices for
    a list of 4 elements.
    When step is given, it specifies the increment (or decrement).
    '''

    def __init__(self, *args):
        '''
        initialize arguments
        '''
        self.start = 0
        self.step = 1

        if len(args) == 1:
            self.stop = args[0]
        elif len(args) == 2:
            self.start, self.stop = args
        elif len(args) == 3:
            self.start, self.stop, self.step = args
        else:
            et = f"myrange expected at most 3 arguments, got {len(args)}"
            raise TypeError(et)

    def __iter__(self):
        '''
        creating iterable object
        '''
        current = self.start

        while (self.step > 0 and current < self.stop) or \
                (self.step < 0 and current > self.stop):
            yield current
            current += self.step

    def __call__(self):
        '''
        return iterable object
        '''
        return iter(self)

for i in Range(10):
    print(i)
