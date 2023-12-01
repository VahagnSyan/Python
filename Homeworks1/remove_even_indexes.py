"""
    Print characters from a string that are
    present at an even index number
    Orginal String is  test_text
    Printing only even index chars
"""


def input_string():
    string = input("Input the string: ")
    return string


string = input_string()

for i in range(0, len(string)):
    # Iterating over string and checking if they are even
    if i % 2 == 0:
        print(string[i])
