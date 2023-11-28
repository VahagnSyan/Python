""" ex2.py
Remove first n characters from a string
Write a program to remove characters from a string starting from zero up to n and return a new string.
"""

text = "Lorem ipsum dolor sit amet"
n = int(input("Enter the number: "))
print(f"Text: {text}")
print(f"Result: {text[n:]}")

