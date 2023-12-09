'''
write functions for the following string operations
  -is_in_str(str_obj, sub_string)
these functions should do the same as a builtin string functions do
'''

def is_in_str(str_obj, sub_string):
    if len(str_obj) < len(sub_string):
        return "Length of string object is less then sub string. Try Again !!"

    count_of_charcters_in_substring = 0

    for i in range(len(str_obj) - len(sub_string) + 1):
        for j in range(len(sub_string)):

            if str_obj[i + j] == sub_string[j]:
                count_of_charcters_in_substring += 1
            else:
                count_of_charcters_in_substring = 0
                break

        if len(sub_string) == count_of_charcters_in_substring:
            return True
    return False


input_string = input("Enter string : ")
substring = input("Enter sub string : ")

while len(input_string) < len(substring):
    print("\nLength of string object is less then sub string. Try Again !!\n")
    input_string = input("Enter string : ")
    substring = input("Enter sub string : ")
    
print( "Is in string : ",is_in_str(input_string, substring))
