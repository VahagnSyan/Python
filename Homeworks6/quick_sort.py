def partition(list, low, high):
    pivot = list[high]
    i = low - 1

    for j in range(low, high):
        if list[j] < pivot:
            i += 1
            list[i], list[j] = list[j], list[i]

    list[i + 1], list[high] = list[high], list[i + 1]

    return i + 1


def quick_sort(list, low, high):
    if low < high:
        pivotIndex = partition(list, low, high)

        quick_sort(list, low, pivotIndex - 1)
        quick_sort(list, pivotIndex + 1, high)

    return list


input_list = []
assert quick_sort(input_list, 0, len(input_list) - 1) == []

input_list = [5, -3, 4, 13, -10, 7]
assert quick_sort(input_list, 0, len(input_list) - 1) == [-10, -3, 4, 5, 7, 13]

input_list = [42]
assert quick_sort(input_list, 0, len(input_list) - 1) == [42]

input_list = [8, 8, 8, 8, 8]
assert quick_sort(input_list, 0, len(input_list) - 1) == [8, 8, 8, 8, 8]

input_list = [1, 2, 3, 4, 5]
assert quick_sort(input_list, 0, len(input_list) - 1) == [1, 2, 3, 4, 5]

input_list = [5, 4, 3, 2, 1]
assert quick_sort(input_list, 0, len(input_list) - 1) == [1, 2, 3, 4, 5]

input_list = [5, -3, 4, -3, -10, 32, 5]
assert quick_sort(input_list, 0, len(input_list) - 1) == [-10, -3, -3, 4, 5, 5, 32]

input_list = [9, 7, 5, 11, 12, 2, 14, 3, 10]
assert quick_sort(input_list, 0, len(input_list) - 1) == [2, 3, 5, 7, 9, 10, 11, 12, 14]
