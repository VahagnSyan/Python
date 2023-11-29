"""
Print characters from a string that are present at an even index number
Orginal String is  test_text
Printing only even index chars
"""

input_string = "test_text" # Magic value


for i in range (0, len(input_string)):
    # Iterating over string and checking if they are even
    if(i % 2 == 0):
        print(input_string[i])