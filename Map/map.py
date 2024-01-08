'''
    map function
'''

def my_map(func, list1, list2):
    '''
    map function to work with two lists
    '''
    it1 = iter(list1) # Creating an iterator for list1
    it2 = iter(list2) # Creating an iterator for list2
    while True:
        try:
            # call function for list values
            yield func(next(it1), next(it2))
        except StopIteration:
            break

def add(num1, num2):
    '''
    return the sum of two numbers
    '''
    return num1 + num2

l1 = [1, 2, 3]
l2 = [4, 5, 6, 7]

print(map(add, l1, l2))
print(my_map(add, l1, l2))
for i in map(add, l1, l2):
    print(i)
