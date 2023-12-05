# write functions for the following string operations
#   -startswith(str_obj, sub_string)
#   -endswith(str_obj, sub_string)
#   -is_in_str(str_obj, sub_string)
# these functions should do the same as a builtin string functions do


def startswith(str_obj, sub_string):
    if len(str_obj) < len(sub_string):
        return "Length of string object is less then sub string. Try Again !!"

    for i in range(len(sub_string)):
        if str_obj[i] != sub_string[i]:
            return False
    return True


string = input("Enter string : ")
substring = input("Enter sub string : ")

print(startswith(string, substring))
