'''
    Filter function
'''

def my_filter(func, iterable):
    for it in iterable:
        if func(it):
            yield it

def is_even(number):
    '''
    This function return number if number is even
    '''
    if number % 2 == 0:
        return number

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
f = my_filter(is_even, numbers)
for i in f:
    print(i)
