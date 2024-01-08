'''
    mapp function for two lists
'''


from operator import add

def mapp(func, first_list, second_list):
    '''
    Make an generator for two lists
    '''
    first_it = iter(first_list)
    second_it = iter(second_list)
    while True:
        try:
            yield func(next(first_it), next(second_it))
        except StopIteration:
            break
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

print(list(mapp(add, list_1, list_2)))
