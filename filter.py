'''
Filter function
'''


def filterr(func, iterable):
    '''
    Return an iterator yielding those items of iterable 
    for which function(item) is true.
    '''
    for i in iterable:
        if func(i):
            yield i


print(list(filterr(lambda x: x % 2 == 0, (1, 2, 3, 4, 5, 6))))
