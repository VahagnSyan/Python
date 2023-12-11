'''
ex 16
Write a function that takes a list with repeating elements and returns a new list with non-repeating elements of the given list.
'''

def remove_duplicates(input_list):
    unique_elements = []
    for element in input_list:
        if input_list.count(element) == 1:
            unique_elements.append(element)
    return unique_elements

# original_list = [1, 2, 2, 6, 3, 4, 4, 5, 3, 4, 4, 5]
# result_list = remove_duplicates(original_list)
# print(result_list)


#Testing version
original_list_1 = [1, 2, 2, 6, 3, 4, 4, 5, 3, 4, 4, 5]
result_1 = remove_duplicates(original_list_1)
assert result_1 == [1, 6], "Test 1 failed"

original_list_2 = [1, 2, 2, 3, 3, 4, 4, 5, 5]
result_2 = remove_duplicates(original_list_2)
assert result_2 == [1], "Test 2 failed"

original_list_3 = [1, 2, 3, 4, 5]
result_3 = remove_duplicates(original_list_3)
assert result_3 == [1, 2, 3, 4, 5], "Test 3 failed"

print("All tests passed!")
