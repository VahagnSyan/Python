'''
task_3
Print characters from a string that are present at an even index number
Orginal String is  test_text
Printing only even index chars

t
s
_
e
t
'''

original_string = "test_text"
even_chars = original_string[::2]

for char in even_chars:
    print(char)