""" ex14.py

    Write a program to count the number of characters in a text
"""


def elements_count(t):
    symbols = list(t)
    result = {symbol: symbols.count(symbol) for symbol in set(symbols)}
    return result

text = input("Enter the text: ")

print(elements_count(text))

