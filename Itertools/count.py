'''
Implement itertools.count function
'''


def countt(start=0, step=1):
    '''
    Return a generator where consecutive values.
    '''
    while True:
        yield start
        start += step


for i in countt(5, 2):
    if i >= 100:
        break
    print(i)
