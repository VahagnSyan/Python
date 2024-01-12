'''
    Cycle function
'''

def my_cycle(iterable):
    while True:
        for i in iterable:
            yield i

l = [1, 2, 3, 4]
a = my_cycle(l)
for i in range(5):
    print(next(a))
