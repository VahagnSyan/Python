'''
    Fibonacci function
'''

# Version 1
def fibonacci_v1(n: int) -> int:
    '''
    This function returns the nth Fibonacci number
    @parm: n: should be int
    ...
    '''
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci_v1(n - 1) + fibonacci_v1(n - 2)

print(fibonacci_v1(10))

# Version 2
def fibonacci_v2(n: int) -> int:
    '''
    This function returns the nth Fibonacci number
    @parm: n: should be int
    ...
    '''
    if n == 1:
        return 0
    if n == 2:
        return 1
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

print(fibonacci_v2(10))
