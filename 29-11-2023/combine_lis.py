def combine_list(list_in_list):
    combined_list = []
    for i in list_in_list:
        for j in i:
            combined_list.append(j)
    return combined_list

input_list = [['a', 'b'], ['c', 'd']]
result = combine_list(input_list)
print("The original List:", input_list)
print("The combined list:", result)
