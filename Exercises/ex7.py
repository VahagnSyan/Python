'''
Startswith(str_obj, sub_string)
'''

def starts_with(str_obj, sub_string):
    return str_obj[:len(sub_string)] == sub_string
        

str_obj = input("Enter the string :")
sub_string = input("Enter the string to chake if the main string starts whith it :")
if starts_with(str_obj, sub_string):
    print(str_obj + " starts with " + sub_string)
else:
    print(str_obj + " is't start with " + sub_string)