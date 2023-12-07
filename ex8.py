'''
ex8
write functions for the following string operations
endswith(str_obj, sub_string)
'''


def ends_with(str_obj, sub_string):
    return str_obj[-len(sub_string):] == sub_string
string_obj = str(input("Enter your text: "))
substring = str(input("Enter a substring: "))

result = ends_with(string_obj, substring)
if result:
    print(f"The string '{string_obj}' ends with '{substring}'")
else:
    print(f"The string '{string_obj}' dosen't ends with '{substring}'")
