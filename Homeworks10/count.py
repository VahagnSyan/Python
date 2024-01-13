"""
    Implement count function from itertools.
"""


def count(start=0, step=1):
    current = start
    while True:
        yield current
        current += step


for num in count(start=10, step=2):
    if num > 20:
        break
    print(num)
