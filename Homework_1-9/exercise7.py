'''
    write functions for the following string operations
    startswith(str_obj, sub_string)
'''

def startswith(str_obj, sub_string):
    return str_obj[:len(sub_string)] == sub_string

str_input = input("Enter the  string: ")
sub_input = input("Enter the substring: ")

result = startswith(str_input, sub_input)
print(f"The <{str_input}> starts with the <{sub_input}> substring: {result}")
