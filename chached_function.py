def fibonacci(n):
    if n <= 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def caching(func):
    nums = {}
    def inner(*n):
        result = []
        for i in n:
            if i in nums:
                result.append(nums[i])
                return nums[i]
            nth = func(i)
            nums[i] = nth
            result.append(nth)
        return result
    inner.__doc__ = func.__doc__
    inner.__name__ = func.__name__
    return inner

cached_fibonacci = caching(fibonacci)
assert cached_fibonacci(1, 2, 3, 10) == [1, 1, 2, 89]
print("All good")
