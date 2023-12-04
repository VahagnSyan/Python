def str_count(input_str):
    dict_count = {}
    for key in input_str:
        dict_count[key] = dict_count.get(key, 0) + 1
    return dict_count


input_str = input("Enter the string: ")
result = str_count(input_str)
print("The count of each element in string -", result)
