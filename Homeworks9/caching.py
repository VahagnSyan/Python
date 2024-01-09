import pickle


def caching(func):
    cache = {}

    def add_cache(*args):
        key = pickle.dumps(args)
        if key not in cache:
            cache[key] = func(*args)
            print(cache[key])

        return cache[key]

    return add_cache


@caching
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@caching
def calculate_square_root(x):
    return x**0.5


@caching
def concatenate_lists(list1, list2):
    return list1 + list2


l1 = [1, 2, 3]
l2 = [2, 3, 4]

print(fibonacci(8))
# print(calculate_square_root(8))
# print(concatenate_lists([1, 2, 3], [4, 2, 3]))
