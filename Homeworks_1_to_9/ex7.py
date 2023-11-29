""" ex7.py

	write functions for the following string operation
	startswith(str_obj, sub_string)

"""

def startswith(str_obj, sub_string):
    return str_obj[:len(sub_string)] == sub_string

print(startswith("abcde", "ab"))

