def chain(*iterables):
    for iterable in iterables:
        yield from iterable

l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']
l3 = (True, False)

print(list(chain(l1, l2, l3)))
