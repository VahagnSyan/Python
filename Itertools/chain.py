'''
Implement itertools.chain function
'''


def chainn(*iterables):
    '''
    Return a generator where elements from the
    first iterable until it is exhausted, then elements from the next
    iterable, until all of the iterables are exhausted.
    '''
    for i in iterables:
        for j in i:
            yield j


for k in chainn([5, 6, 7], (1, 7, 9)):
    print(k)
