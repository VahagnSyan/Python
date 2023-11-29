"""write functions for the following string operations
startswith(str_obj, sub_string)
"""


def startswith(str_obj, sub_string):
    return str_obj[:len(sub_string)] == sub_string

string_obj = input("Enter some text: ")
substring = input("Enter text to check if previous text starts with it: ")
if startswith(string_obj, substring):
    print(f"{string_obj} is start with {substring}")
else:
    print(f"{string_obj} is not start with {substring}")