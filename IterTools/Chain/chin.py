'''
    Chain function
'''

def chain(*args):
    '''
    Return a chain object whose .__next__() method returns elements from the
    first iterable until it is exhausted, then elements from the next
    iterable, until all of the iterables are exhausted.
    '''
    for i in args:
        for j in i:
            yield j


test = chain([1, 2, 3, 4], [5, 6, 7, 8])
for t in test:
    print(t, end=' ')
print()
