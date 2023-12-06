#function that remove repeating elements of the given list 

def make_list(list):
    non_repeating_list = []
    for element in list:
        if element not in non_repeating_list:
            non_repeating_list.append(element)
    return non_repeating_list

list = eval(input("Enter the list: "))
non_repeating_list = make_list(list)

print(non_repeating_list)
