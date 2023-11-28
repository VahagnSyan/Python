"""write functions for the following string operations
startswith(str_obj, sub_string)
"""

def startswith(str_obj, sub_string):
    return str_obj[:len(sub_string)] == sub_string

print(startswith("Qwerty", "Qw"))