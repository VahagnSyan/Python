# write functions for the following string operations
#   -is_in_str(str_obj, sub_string)
# these functions should do the same as a builtin string functions do


def is_in_str(str_obj, sub_string):
    if len(str_obj) < len(sub_string):
        return "Length of string object is less then sub string. Try Again !!"

    temp = 0
    count = 0
    for i in range(len(str_obj) - len(sub_string) + 1):
        for j in range(len(sub_string)):
            if str_obj[i + j] == sub_string[j]:
                temp += 1
            else:
                temp = 0
                break
        if len(sub_string) == temp:
            return True
    return False


string = input("Enter string : ")
substring = input("Enter sub string : ")

print(is_in_str(string, substring))
