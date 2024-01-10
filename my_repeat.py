def my_cycle(itearable, count):
    for _ in range(count):
        for i in itearable:
            yield  i

   
a = my_cycle([1, 2], 2)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
