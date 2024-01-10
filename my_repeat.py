def my_cycle(itearable, count):
    for _ in range(count):
        yield itearable


a = my_cycle("aaa", 2)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
