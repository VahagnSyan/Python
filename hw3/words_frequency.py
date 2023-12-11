def count_word_frequency(paragraph):
    words = paragraph.split()

    word_frequency = {}
    
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1

    return word_frequency

paragraph = input("Input the paragraph: ")

word_frequency_dict = count_word_frequency(paragraph)

print(word_frequency_dict)

