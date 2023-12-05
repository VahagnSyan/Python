# write functions for the following string operations
#   -endswith(str_obj, sub_string)
# these functions should do the same as a builtin string functions do


def endswith(str_obj, sub_string):
    if len(str_obj) < len(sub_string):
        return "Length of string object is less then sub string. Try Again !!"

    for i in range(len(sub_string) - 1, -1, -1):
        if str_obj[len(str_obj) - len(sub_string) + i] != sub_string[i]:
            return False
    return True


string = input("Enter string : ")
substring = input("Enter sub string : ")

print(endswith(string, substring))
