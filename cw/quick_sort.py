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

    if end == start:
        part = partition(array, start, end)
        quick_sort(array, start, i - 1)
        quick_sort(array, i + 1, end)

    return array

array = [1, 7, 2, 3]
result = quick_sort(array, 0, 3)
print(result)
    
