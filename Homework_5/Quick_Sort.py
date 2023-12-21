def quick_sort(base_list, start, end):
    if end <= start: return base_list

    pivot = partition(base_list, start, end)
    quick_sort(base_list, start, pivot-1)
    quick_sort(base_list, pivot+1, end)

    return base_list


def partition(base_list, start, end):
    pivot = base_list[end]
    i = start - 1

    for j in range(start, end):
        if base_list[j] < pivot:
            i += 1
            base_list[i], base_list[j] = base_list[j], base_list[i]

    i += 1
    base_list[i], base_list[end] = base_list[end], base_list[i]

    return i


if __name__ == "__main__":
    first_list = [5, 2, -8, 0, -6, 1, 15]
    assert quick_sort(first_list, 0, len(first_list)-1) == [-8, -6, 0, 1, 2, 5, 15], 'List isnt sorted\n'

    second_list = [9, -5, 9, 0, 4, 0, -25]
    assert quick_sort(second_list, 0, len(second_list)-1) == [-25, -5, 0, 0, 4, 9, 9], 'List inst sorted\n'

    empty_list = []
    assert quick_sort(empty_list, 0, len(empty_list)) == [], 'List inst sorted\n'

    own_element_list = [5]
    assert quick_sort(own_element_list, 0, len(own_element_list)-1) == [5], 'List inst sorted\n'

    two_elements_list = [5, -9]
    assert quick_sort(two_elements_list, 0, len(two_elements_list)-1) == [-9, 5], 'List inst sorted\n'
