def remove_duplicates(final_list):
    upd_elements = []
    for i in final_list:
        if i not in upd_elements:
            upd_elements.append(i)
    return upd_elements

input_list = input("Enter the elements of the array seperated by space: ")
final_list = input_list.split()

result = remove_duplicates(final_list)
print(result)
