"""
    Create dictonary, where keys is text symbols and values are their counts
"""

text = 'aaa fk fkf klf f'
quantity = {}

def count_frequency(text):
    for letter in text:
        if letter in quantity:
            quantity[letter] += 1
        else:
            quantity[letter] = 1

    print(quantity)

count_frequency(text)