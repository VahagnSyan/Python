'''
ex 16
Write a function that takes a list with repeating elements and returns a new list with non-repeating elements of the given list.
'''

def remove_duplicates(input_list):
    unique_elements = []
    for element in input_list:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements

original_list = [1, 2, 2, 6,3, 4, 4, 5, 3, 4, 4, 5]
result_list = remove_duplicates(original_list)
print(result_list)
