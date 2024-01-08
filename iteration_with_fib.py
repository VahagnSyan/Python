def my_map(func, iterable):
    for item in iterable:
        yield func(item)


def square(num):
    return num ** 2

listt = [1, 2, 3, 4, 5]
result_iterator = my_map(square, listt)
for result in result_iterator:
    print(result)
