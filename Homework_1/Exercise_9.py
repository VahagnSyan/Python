"""write functions for the following string operations
is_in_str(str_obj, sub_string)
"""

def is_in_str(str_obj, sub_string):
    for i in range(len(str_obj)):
        if str_obj[i : i+len(sub_string)] == sub_string:
            return True
    
    return False
        

print(is_in_str("abcdef", "abc"))