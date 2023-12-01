"""
    Implement built-in function 
    is_in_str(str_obj, sub_string)
"""

input_string = "Hello World!"  # Magic Value
input_substring = "rld"  # Magic Value


def is_in_str(str_obj, sub_string):
    first_match_index = str_obj.find(sub_string[0])

    if first_match_index == -1:
        return False

    if str_obj[first_match_index : first_match_index + len(sub_string)] == sub_string:
        return True
    else:
        return is_in_str(str_obj[first_match_index + 1 :], sub_string)


print(is_in_str(input_string, input_substring))
