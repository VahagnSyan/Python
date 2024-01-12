'''
Implement itertools.accumulate function
'''


from operator import mul


def accumulatee(iterable, func=None):
    '''
    Return generator of accumulated sums 
    (or other binary function results).
    '''
    def add(a, b):
        '''
        Return sum of a and b
        '''
        return a + b

    if func is None:
        func = add
    first_it = iter(iterable)
    try:
        result = next(first_it)
        yield result
        while True:
            try:
                result = func(result, next(first_it))
                yield result
            except StopIteration:
                break
    except StopIteration:
        pass

some_iterable = [1, 2, 3, 0, 14]
accum = accumulatee(some_iterable, mul)
for i in accum:
    print(i)
