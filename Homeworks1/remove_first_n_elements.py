"""
    Remove first n characters from a string
    Write a program to remove characters from
    a string starting from zero up to n and return a new string.
"""


def input_string():
    string = input("Input the string: ")
    return string


def input_character_count():
    characters_count = int(input("Input characters count to remove: "))
    return characters_count


string = input_string()
characters_count = input_character_count()

string = string[characters_count:]  # Slices input string starting from nth position

print(string)
