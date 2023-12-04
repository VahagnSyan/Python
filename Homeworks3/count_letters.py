"""
    Count letters in string and add them to dictionary
"""


def input_string():
    string = input("Input the string: ")
    return string


string = input_string()


def print_letters_count(letters_count):
    for letter, count in letters_count.items():
        print(f"Letter - {letter} occurs {count} times in given string")


def count_letters(string):
    letters_count = {}

    for char in string:
        letters_count[char] = string.count(char)

    print_letters_count(letters_count)


count_letters(string)
