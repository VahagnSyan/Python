'''
    map function
'''


def my_map(func, *args):
    """
    Map function to work with a variable number of lists.
    """
    iterators = [iter(lst) for lst in args]

    while True:
        try:
            # Call function for values from each list
            yield func(*[next(iterator) for iterator in iterators])
        except StopIteration:
            break

def add(num1, num2):
    '''
    return the sum of two numbers
    '''
    return num1 + num2

l1 = [1, 2, 3]
l2 = [4, 5, 6, 7]

for i in map(add, l1, l2):
    print(i)
