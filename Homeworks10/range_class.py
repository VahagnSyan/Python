"""
    Range class implementation.    
"""


class Range:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            start, stop = 0, start
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        current = self.start
        while current < self.stop:
            yield current
            current += self.step


r = Range(5, 15, 2)
result = list(r)
assert result == [5, 7, 9, 11, 13]

r = Range(3, 8)
result = list(r)
assert result == [3, 4, 5, 6, 7]

r = Range(1, 10, 3)
result = list(r)
assert result == [1, 4, 7]
