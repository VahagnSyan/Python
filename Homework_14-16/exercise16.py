'''
    Write a function that receives a list with repeated elements and
    returns a new list with non-repeating elements of the given list.

'''

def non_repeating_list(list):
    return [x for x in list if list.count(x) == 1]

list = [True, 1, 2, 3, False,  "hello", "hello"]
print(non_repeating_list(list))

