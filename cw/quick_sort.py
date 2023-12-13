def quick_sort(array, start, end):


    def partition(array, start, end):
        pivot = array[end]
        i = start - 1
        for j in range(start, end):
            if array[j] < pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[end] = array[end], array[i + 1]
        return i + 1

    if end > start:
        i =  (start + end) // 2
        part = partition(array, start, end)
        quick_sort(array, start, i - 1)
        quick_sort(array, i + 1, end)

    return array
assert quick_sort([], 0, 0) == [], 'Assertion error: [] != []'
assert quick_sort([1], 0, 0) == [1], 'Assertion error: [1] != [1]'
assert quick_sort([-1], 0, 0) == [-1], 'Assertion error: [-1] != [-1]'
assert(
        quick_sort([-2, -1], 0, 1) == [-2, -1]
), 'Assertion error: [-2, -1] != [-2, -1]'
assert quick_sort([2, 1], 0, 1) == [1, 2], 'Assertion error: [2, 1] != [1, 2]'

print("All assertions passed!!!")
