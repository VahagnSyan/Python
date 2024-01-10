def my_cycle(itearable):
    while True:
        for i in itearable:
            yield  i

        
a = my_cycle([1, 2])
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

