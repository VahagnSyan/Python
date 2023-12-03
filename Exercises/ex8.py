'''
endswith(str_obj, sub_string)
'''

def ends_with(str_obj, sub_string):
   return str_obj[-len(sub_string):] == sub_string


str_obj = input("Enter the string :")
sub_string = input("Enter the string to chake if the main string ends whith it :")
if ends_with(str_obj, sub_string):
    print(str_obj + " ends with " + sub_string)
else:
    print(str_obj + " is't end with " + sub_string)