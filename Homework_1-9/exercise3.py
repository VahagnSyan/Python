'''
    Print characters from a string that are present at an even index number
    Orginal String is  test_text
    Printing only even index chars

    t
    s
    _
    e
    t
'''

string = input("Enter a string: ")
even_chars = string[::2]

print("Printing only even index chars\n")
for char in even_chars:
    print(char)


