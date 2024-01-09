def my_filter(function, iterable):
    for i in iterable:
        if function(i):
            yield i


a = my_filter(lambda x: x % 2 == 0, range(10, 100))
print(list(a))

