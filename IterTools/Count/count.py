'''
    Count function
'''

def count(first=0, step=1):
    '''
    Return a count object whose .__next__() method returns consecutive values.
    '''
    while True:
        yield first
        first += step

for i in count(10):
    print(i)
    if i == 20:
        break
