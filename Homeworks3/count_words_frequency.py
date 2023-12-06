"""
    Count words in string and add them to dictionary
"""


def input_string():
    string = input("Input the string: ")
    return string


string = input_string()


def print_words_count(words_count):
    for letter, count in words_count.items():
        print(f"{letter} | {count}")


def count_words(string):
    words_count = {}
    splitted_string = string.split()

    for word in splitted_string:
        words_count[word] = string.count(word)

    print_words_count(words_count)


count_words(string)
