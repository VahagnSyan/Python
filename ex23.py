def my_range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0

    current = start

    if step > 0:
        while current < stop:
            yield current
            current += step
    elif step < 0:
        while current > stop:
            yield current
            current += step

for i in my_range(2, 10, 2):
    print(i)
