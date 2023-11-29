"""Print characters 
from a string that are present at an even index number
"""


input_text = input("Enter some text: ")
print('\n'.join(input_text[::2]))