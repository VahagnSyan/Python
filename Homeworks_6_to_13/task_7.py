'''
    task 7
    startswith(str_obj, sub_string)
'''

def startswith(str_obj, sub_string):
    return str_obj[:len(sub_string)] == sub_string

string_obj = input('Enter any string: ')
substring = input('Enter the substring: ')

print(f'\nChecking if "{string_obj}" starts with "{substring}"?...')

if startswith(string_obj, substring):
    print('Result ---> TRUE')
else:
    print('Result ---> FALSE')

