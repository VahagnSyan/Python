'''
ex.7, ex.8, ex.9
Write functions for the following string operations:
startswith(str_obj, sub_string)
endswith(str_obj, sub_string)
is_in_str(str_obj, sub_string)
These functions should do the same as the built-in string functions do
'''

# starts_with_obj
def starts_with_obj(string, sub_string):
    return string[:len(sub_string)] == sub_string

# ends_with_obj
def ends_with_obj(string, sub_string):
    return string[-len(sub_string):] == sub_string

# is_in_string
def is_in_string(string, sub_string):
    len_string, len_substring = len(string), len(sub_string)
    for i in range(len_string - len_substring + 1):
        if string[i:i + len_substring] == sub_string:
            return True
    return False

string = str(input("Input the string: "))
sub_string = str(input("Input the substring: "))

if starts_with_obj(string, sub_string):
    print(f"The string starts with {sub_string}")
else:
    print(f"The string does NOT start with {sub_string}")

if ends_with_obj(string, sub_string):
    print(f"The string ends with {sub_string}")
else:
    print(f"The string does NOT end with {sub_string}")

if is_in_string(string, sub_string):
    print(f"There is {sub_string}")
else:
    print(f"There is NO {sub_string}")

