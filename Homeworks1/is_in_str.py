"""
    Implement built-in function 
    is_in_str(str_obj, sub_string)
"""


def input_string():
    string = input("Input the string: ")
    return string


def input_substring():
    string = input("Input the substring: ")
    return string


string = input_string()
sub_string = input_substring()


def is_in_str(str_obj, sub_string):
    first_match_index = str_obj.find(sub_string[0])

    if first_match_index == -1:
        return False

    if str_obj[first_match_index : first_match_index + len(sub_string)] == sub_string:
        return True
    else:
        return is_in_str(str_obj[first_match_index + 1 :], sub_string)


print(is_in_str(string, sub_string))
