""" ex3.py

Print characters from a string that are present at an even index number

Orginal String is  test_text
Printing only even index chars
"""

text = input("Enter your text: ")
print(text)
print("\n".join(text[::2]))

