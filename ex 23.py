def my_range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0

    result = []
    current = start

    if step > 0:
        while current < stop:
            result.append(current)
            current += step
    elif step < 0:
        while current > stop:
            result.append(current)
            current += step

    return result

for i in my_range(2, 10, 2):
    print(i)
