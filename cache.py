'''
    Caching concept
'''


def cache(func):
    '''
    Caching function, returns function
    '''
    visited = {}
    def inner(*args):
        '''
        '''
        if args in visited:
            return visited[args]
        nth = func(*args)
        visited[args] = nth
        print(f'visited: {visited}')
        return nth
    inner.__doc__ = func.__doc__
    inner.__name__ = func.__name__
    return inner


@cache
def fib(n):
    '''
    Returns the number th Fibonacci term
    '''
    if n in (1, 2):
        return 1
    return fib(n-1) + fib(n-2)


print(fib(500))
