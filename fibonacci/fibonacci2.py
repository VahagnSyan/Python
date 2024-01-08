'''
    Fibonacci function
'''

def fibonacci(n: int) -> int:
    '''
        This function returns the nth Fibonacci element
        @parm: n: should be int
        ...
    '''
    if n in (0, 1):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))
