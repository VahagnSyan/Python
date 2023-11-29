"""
Implement built-in function 
startswith(str_obj, sub_string)
"""

input_string = "Hello World!" # Magic Value
input_substring = "He" # Magic Value


def startswith(str_obj, sub_string):
    # Checking if substring is the same as from 0 index to length of substring
    # And returning value
    return True if str_obj[0:len(sub_string)] == sub_string else False


print(startswith(input_string, input_substring))