'''
def quicksort and its asserts 
'''

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return quicksort(less) + equal + quicksort(greater)


my_list = [3, 6, 8, 10, 1, 2, 1, 2.5]
sorted_list = quicksort(my_list)
assert sorted_list == [1, 1, 2, 2.5, 3, 6, 8, 10], "Assertion 1"
print(sorted_list)

my_list2 = []
sorted_list2 = quicksort(my_list2)
assert sorted_list2 == [], "Assertion 2"
print(sorted_list2)

my_list3 = [1]
sorted_list3 = quicksort(my_list3)
assert sorted_list3 == [1], "Assertion 3"
print(sorted_list3)

my_list5 = [-2, -5, 0, 3]
sorted_list5 = quicksort(my_list5)
assert sorted_list5 == [-5, -2, 0, 3], "Assertion 5"
print(sorted_list5)
