"""write functions for the following string operations
is_in_str(str_obj, sub_string)
"""


def is_in_str(str_obj, sub_string):
    for i in range(len(str_obj)):
        if str_obj[i : i+len(sub_string)] == sub_string:
            return True
    
    return False
        
string_obj = input("Enter some text: ")
substring = input("Enter the text to check if the previous text contains it: ")
if is_in_str(string_obj, substring):
    print(f"{substring} is in {string_obj}")
else:
    print(f"{substring} is not in {string_obj}")