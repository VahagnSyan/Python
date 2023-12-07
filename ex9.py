'''
ex.9
write functions for the following string operations
is_in_str(str_obj, sub_string)

'''


def is_in_str(str_obj, sub_string):
    len_substring = len(sub_string)
    for i in range(len(str_obj) - len_substring + 1):
        if str_obj[i:i + len_substring] == sub_string:
            return True
    return False
string_obj = str(input("Enter your text: "))
substring = str(input("Enter a substring: "))

result = is_in_str(string_obj, substring)
if result:
    print(f"The string '{string_obj}' is in '{substring}'")
else:
    print(f"The string '{string_obj}' ism't in '{substring}'")

