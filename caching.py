def caching(func):
    nums = {}
    def inner(*n):
        argument_type = func.__annotations__
        try:
            if all(isinstance(val, argument_type[param]) for param, val in zip(argument_type, n)):
                if n in nums:
                    return nums[n]
                nth = func(*n)
                nums[n] = nth
                return nth
            else:
                raise TypeError
        except TypeError:
            print(f"Invalid argument types for function {func.__name__}")
            return
    return inner
    
@caching
def fib(n:int):
    if n == 0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)
    
fib = caching(fib)
print(fib(5))

@caching
def mul(n1:float, n2:float):
    return n1 * n2
    
mul = caching(mul)
print(mul(7.2, 2.4))
