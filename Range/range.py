'''
Range class implementation
'''


class Range:
    '''
    Return an object that produces a sequence of integers from start
    to stop by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
    start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
    These are exactly the valid indices for a list of 4 elements.
    When step is given, it specifies the increment (or decrement).
    '''


    def __init__(self, *args):
        '''
        Initialize start, end, step and current variables
        '''
        self.start = 0
        self.step = 1
        self.__current = None
        if len(args) == 1:
            self.end = args[0]
        elif len(args) == 2:
            self.start, self.end = args
        elif len(args) == 3:
            self.start, self.end, self.step = args
        else:
            raise TypeError(f'rangee expected at 1 to 3 arguments, '
                            f'got {len(args)}')

    def __iter__(self):
        '''
        Create iterator for range
        '''
        self.__current = self.start
        return self

    def __next__(self):
        '''
        Return range value and change pointer to next
        '''
        if (self.step > 0 and self.__current < self.end) or \
            (self.step < 0 and self.__current > self.end):
            result = self.__current
            self.__current += self.step
            return result
        raise StopIteration


obj = Range(5, 10)
print(f'{obj.start = }', f'{obj.step = }', f'{obj.end = }', sep='\n')
for i in obj:
    print(i)
