'''
write functions for the following string operations
  -startswith(str_obj, sub_string)
these functions should do the same as a builtin string functions do
'''


def startswith(str_obj, sub_string):
    for i in range(len(sub_string)):
        if str_obj[i] != sub_string[i]:
            return False
    return True


input_string = input("Enter string : ")
substring = input("Enter sub string : ")

while len(input_string) < len(substring):
    print("\nLength of string object is less then sub string. Try Again !!\n")
    input_string = input("Enter string : ")
    substring = input("Enter sub string : ")

print("Srartswift is", startswith(input_string, substring))
