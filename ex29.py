def count(start=0, step=1):
    current = start
    while True:
        yield current
        current += step

counter = count(5, 2)
for _ in range(5):
    print(next(counter))
