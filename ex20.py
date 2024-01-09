def convert_to_tuple(value):
    if isinstance(value, list):
        return tuple(value)
    return value

def caching(func):
    numbers = {}
    def inner(*n):
        # Check types of arguments based on the function signature
        signature = func.__annotations__
        try:
            if all(isinstance(val, signature[param]) for param, val in zip(signature, n)):
                key = tuple(convert_to_tuple(val) for val in n)
                if key in numbers:
                    return numbers[key]
                result = func(*n)
                numbers[key] = result
                return result
            else:
                raise TypeError
        except TypeError:
            print(f"Invalid argument types for function {func.__name__}")
            return
    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner

@caching
def fib(num: int):
    '''
    This function calculates the n-th element of Fibonacci sequence.
    '''
    if num == 0 or num == 1:
        return 1
    return fib(num - 1) + fib(num - 2)

@caching
def add(arg1: float, arg2: float):
    '''
    This function returns arg1 + arg2.
    '''
    return arg1 + arg2

@caching
def multiply_by_two(numbers: list):
    '''
    This function multiplies each element in the input list by 2 and returns a new list.
    '''
    result = [num * 2 for num in numbers]
    return result

# caching with the Fibonacci function
fib = caching(fib)
result_fib = fib(5)
print(f"Fibonacci result: {result_fib}")

# caching with the add function
add = caching(add)
result_add = add(2.5, 42.5)
print(f"Add result: {result_add}")

# caching with the multiply_by_two function
multiply_by_two = caching(multiply_by_two)
result_multiply_by_two = multiply_by_two([1, 2, 3, 4])
print(f"Result of multiply_by_two function: {result_multiply_by_two}")
