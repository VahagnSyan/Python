""" ex8.py

	write functions for the following string operation
	endswith(str_obj, sub_string)

"""

def endswith(str_obj, sub_string):
    return str_obj[len(str_obj) - len(sub_string):] == sub_string

print(endswith("abcde", "de"))

