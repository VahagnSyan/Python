def my_cycle(iterable):
    while True:
        for element in iterable:
            yield element

l = [1, 2, 3]
cycle_generator = my_cycle(l)

for i in range(10):
    print(next(cycle_generator))
