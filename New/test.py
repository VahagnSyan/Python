'''
    Fibonacci function with caching
'''

import timeit

def fib(n: int) -> int:
    '''
    This function returns the n-th Fibonacci element
    @parm: n: should be int
    '''
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)

def caching(func):
    '''
    This is a caching function
    returns a inner function
    '''
    visited = {}
    def inner(n: int) -> int:
        '''
        '''
        if n in visited:
            return visited[n]
        nth = func(n)
        visited[n] = nth
        print(f'visited: {visited}')
        return nth
    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner

fib1 = caching(fib)
print(timeit.repeat(lambda: fib1(5), number=100000, repeat=3))
print(timeit.repeat(lambda: fib1(8), number=100000, repeat=3))
print(timeit.repeat(lambda: fib1(10), number=100000, repeat=3))
