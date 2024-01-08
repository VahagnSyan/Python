'''
    Caching function
'''

import timeit

def caching(func):
    '''
    This is a caching function
    returns a inner function
    '''
    visited = {}
    def inner(*n):
        '''
        '''
        if n in visited:
            return visited[n]
        nth = func(*n)
        visited[n] = nth
        print(f'visited: {visited}')
        return nth
    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner

@caching
def fib(n: int) -> int:
    '''
    This function returns the n-th Fibonacci element
    @parm: n: should be int
    '''
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)

#fib1 = caching(fib)
#print(timeit.repeat(lambda: fib1(30), number=100000, repeat=3))
#print(timeit.repeat(lambda: fib1(40), number=100000, repeat=3))
#print(timeit.repeat(lambda: fib(50), number=100000, repeat=3))
