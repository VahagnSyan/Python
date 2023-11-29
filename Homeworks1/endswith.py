"""
Implement built-in function 
endswith(str_obj, sub_string)
"""

input_string = "Hello World!" # Magic Value
input_substring = "d!" # Magic Value


def endswith(str_obj, sub_string):
    # Checking if substring is the same startring from
    # substring length subtracted length of string
    # to end of string
    # and returning value
    return True if str_obj[-len(sub_string):] == sub_string else False


print(endswith(input_string, input_substring))