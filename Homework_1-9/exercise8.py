'''
	write functions for the following string operation
	endswith(str_obj, sub_string)
'''
        
def endswith(str_obj, sub_string):
    return str_obj[-len(sub_string):] == sub_string

str_input = input("Enter the  string: ")
sub_input = input("Enter the substring: ")

result = endswith(str_input, sub_input)
print(f"The <{str_input}> ends with the <{sub_input}> substring: {result}")
 