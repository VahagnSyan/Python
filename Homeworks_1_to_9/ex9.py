""" ex9.py

	write functions for the following string operation
	is_in_str(str_obj, sub_string)

"""

def is_in_str(str_obj, sub_string):
    for i in range(0, len(str_obj) - 1):
        if str_obj[i:i + len(sub_string)] == sub_string:
            return True
    return False

print(is_in_str("abcde", "cd"))

