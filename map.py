'''
    mapp function for two lists
'''


from operator import add


def mapp(func, *iterables):
    '''
    Return a generator that computes the function using arguments from
    each of the iterables.
    '''
    iterators = [iter(i) for i in iterables]
    while True:
        try:
            yield func(*[next(it) for it in iterators])
        except StopIteration:
            break


list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

print(list(mapp(add, list_1, list_2, [5, 8, 9])))
