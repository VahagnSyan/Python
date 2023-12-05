""" ex15.py

    Գրեք ծրագիր, որը կհաշվի պարագրաֆում  օգտագործված բառերի հաճախականությունը
"""


def words_count(p_ph):
    words = p_ph.split()
    result = {word: words.count(word) for word in set(words)}
    print(result)

paragraph = input("Enter the paragraph: ")
words_count(paragraph)

