'''
def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]

my_list = [3, 6, 8, 10, 1, 2, 1]
quicksort(my_list, 0, len(my_list) - 1)
print(my_list)
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
