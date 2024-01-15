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
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if (self.step > 0 and self.current >= self.stop) or (self.step < 0 and self.current <= self.stop):
            raise StopIteration
        else:
            current_value = self.current
            self.current += self.step
            return current_value


for i in MyRange(2, 10, 2):
    print(i)
