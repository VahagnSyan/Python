'''
    Accumulate function
'''

def myaccumulate(iterable, func=None):
    '''
    Return series of accumulated sums (or other binary function results).
    '''
    def add(a, b):
        '''
        Returns sum of a and b
        '''
        return a + b

    if func is None:
        func = add
    it = iter(iterable)
    try:
        argument = next(it)
        yield argument
        while True:
            try:
                argument = func(argument, next(it))
                yield argument
            except StopIteration:
                break
    except StopIteration:
        pass

l = [1, 2, 3, 4, 5]
test = myaccumulate(l)
for i in test:
    print(i, end=' ')
print()
