"""write functions for the following string operations
endswith(str_obj, sub_string)
"""

def endswith(str_obj, sub_string):
    return str_obj[len(str_obj)-len(sub_string) :] == sub_string

print(endswith("Qwerty", "ty"))