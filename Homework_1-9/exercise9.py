'''
	write functions for the following string operation
	is_in_str(str_obj, sub_string)
'''

def is_in_str(str_obj, sub_string):
    if len(sub_string) > len(str_obj):
        return False
    
    i = 0
    while i <= len(str_obj) - len(sub_string):
        if str_obj[i:i + len(sub_string)] == sub_string:
            return True
        i += 1
    
    return False

str_input = input("Enter the  string: ")
sub_input = input("Enter the substring: ")

result = is_in_str(str_input, sub_input)
print(f"The <{str_input}> sting includes the <{sub_input}> substring: {result}") 
