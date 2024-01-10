'''
Range with class
'''

class MyRange:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            stop = start
            start = 0

        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        current = self.start

        if self.step > 0:
            while current < self.stop:
                yield current
                current += self.step
        elif self.step < 0:
            while current > self.stop:
                yield current
                current += self.step

for i in MyRange(2, 10, 2):
    print(i)
