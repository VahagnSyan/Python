'''
    ex.8
    endswith(str_obj, sub_string)
'''

def endswith(str_obj, sub_string):
    return str_obj[len(sub_string):] == sub_string

string_obj = input('Enter any string: ')
substring = input('Enter the substring: ')

print(f'\nChecking if "{string_obj}" ends with "{substring}"?...')

if endswith(string_obj, substring):
    print('Result ---> TRUE')
else:
    print('Result ---> FALSE')
