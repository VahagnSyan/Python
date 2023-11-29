'''
The program is about manual writing of string 3 operations in functions
'''


def starts_with(str_obj, sub_string):
    return str_obj.startswith(sub_string)

def ends_with(str_obj, sub_string):
    return str_obj.endswith(sub_string)

def is_in_str(str_obj, sub_string):
    return sub_string in str_obj

input_str = "Hello Poxos"

print(starts_with(input_str, "Hello"))  # True

print(ends_with(input_str, "Poxos"))  # True

print(is_in_str(input_str, "Po"))  # True

