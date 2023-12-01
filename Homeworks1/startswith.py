"""
    Implement built-in function 
    startswith(str_obj, sub_string)
"""


def input_string():
    string = input("Input the string: ")
    return string


def input_substring():
    string = input("Input the substring: ")
    return string


string = input_string()
sub_string = input_substring()


def startswith(str_obj, sub_string):
    # Checking if substring is the same as from 0 index to length of substring
    # And returning value
    return True if str_obj[0 : len(sub_string)] == sub_string else False


print(startswith(string, sub_string))
