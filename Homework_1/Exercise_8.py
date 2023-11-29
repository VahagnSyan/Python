"""write functions for the following string operations
endswith(str_obj, sub_string)
"""

def endswith(str_obj, sub_string):
    return str_obj[len(str_obj)-len(sub_string) :] == sub_string

string_obj = input("Enter some text: ")
substring = input("Enter text to check if previous text ends with it: ")
if endswith(string_obj, substring):
    print(f"{string_obj} is end with {substring}")
else:
    print(f"{string_obj} is not end with {substring}")