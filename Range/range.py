'''
    Range function
'''

def my_range(*args):
    '''
    Return an generator that produces a sequence of integers from start
    (inclusive) to stop (exclusive) by step.  range(i, j)
    produces i, i+1, i+2, ..., j-1. start defaults to 0, and stop is omitted!
    range(4) produces 0, 1, 2, 3.These are exactly the valid indices for
    a list of 4 elements.
    When step is given, it specifies the increment (or decrement).
    '''
    start = 0
    step = 1
    if len(args) == 1:
        stop = args
    elif len(args) == 2:
        start, stop == args
    elif len(args) == 3:
        start, stop, step = args
    else:
        et = "my_range expected at most 3 arguments, got {}".format(len(args)))
        raise TypeError(et)
    current = start
    while (step > 0 and current < stop) or (step < 0 and current > stop):
        yield current
        current += step

for i in my_range(10, 1, -2, 4):
    print(i)
