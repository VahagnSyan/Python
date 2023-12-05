def word_count_frequency(paragraph):
    words = paragraph.lower().split()

    word_frequency = {}

    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1

    return word_frequency

paragraph = 'Hello Hello abg abg bah ldksa ldsd la la la'
result = word_count_frequency(paragraph)
print(result)
