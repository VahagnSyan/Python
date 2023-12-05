# Returns a new list with non-repeating elements of the given list.
def get_uniq_list(some_list):
    element_count = {}
    uniq_list = []

    for i in some_list:
        element_count[i] = element_count.get(i, 0) + 1

    for key, value in element_count.items():
        if value == 1:
            uniq_list.append(key)

    return uniq_list

some_list = [True, 1, 2, 3, 1, False, True, "hello", "hello", 7, b'fstx']
print(get_uniq_list(some_list))
