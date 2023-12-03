'''
is_in_str(str_obj, sub_string)
'''

def is_in_str(str_obj, sub_string):
      for i in range(len(str_obj)):
        if str_obj[i:i+len(sub_string)] == sub_string:
            return True
      return False

str_obj = input("Enter the string :")
sub_string = input("Enter the string to chake if it is in the main string :")
if is_in_str(str_obj, sub_string):
    print(sub_string + " is in the  " + str_obj)
else:
    print(sub_string + " is't in the " + str_obj)