'''
Range function
'''


def rangee(*args):
    '''
    Return a generator that produces a sequence of integers 
    from start (inclusive) to stop (exclusive) by step.  
    range(i, j) produces i, i+1, i+2, ..., j-1.
    start defaults to 0, and stop is omitted!
    '''
    start = 0
    step = 1
    end = 0
    if len(args) == 1:
        end = args[0]
    elif len(args) == 2:
        start, end = args
    elif len(args) == 3:
        start, end, step = args
    else:
        raise TypeError(f'rangee expected at 1 to 3 arguments, '
                        f'got {len(args)}')
    current = start
    while (current < end and step > 0) or (current > end and step < 0):
        yield current
        current += step


for i in rangee(-20, -4, 5):
    print(i)
