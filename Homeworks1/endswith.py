"""
    Implement built-in function 
    endswith(str_obj, sub_string)
"""


def input_string():
    string = input("Input the string: ")
    return string


def input_substring():
    string = input("Input the substring: ")
    return string


string = input_string()
sub_string = input_substring()


def endswith(str_obj, sub_string):
    # Checking if substring is the same startring from
    # substring length subtracted length of string
    # to end of string
    # and returning value
    return True if str_obj[-len(sub_string) :] == sub_string else False


print(endswith(string, sub_string))
