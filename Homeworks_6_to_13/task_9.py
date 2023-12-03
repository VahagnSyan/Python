'''
    ex.9
    is_in_str(str_obj, sub_string)
'''

def is_in_str(str_obj, sub_string):
    return sub_string in str_obj

string_obj = input('Enter any string: ')
substring = input('Enter the substring: ')

print(f'\nChecking if "{substring}" is in "{string_obj}"?...')

if is_in_str(string_obj, substring):
    print('Result ---> TRUE')
else:
    print('Result ---> FALSE')
