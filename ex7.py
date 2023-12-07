'''
ex7
write functions for the following string operations
startswith(str_obj, sub_string)
'''


def starts_with(str_obj, sub_string):
    return str_obj[:len(sub_string)] == sub_string

string_obj = str(input("Enter your text: "))
substring = str(input("Enter substring: "))

result = starts_with(string_obj, substring)
if result:
    print(f"The string '{string_obj}' starts with '{substring}'")
else:
    print(f"The string '{string_obj}' doesn't starts with '{substring}'")
