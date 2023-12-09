'''
Գրեք ծրագիր, որը կհաշվի պարագրաֆում  օգտագործված բառերի հաճախականությունը
'''


def count_word_frequency(paragraph):
    
    words = paragraph.split()
    word_frequency = {}

    for word in words:
    
        word = word.strip('.,?!/;:').lower()
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    return word_frequency


paragraph = input("Enter paragraph: \n")

frequency_result = count_word_frequency(paragraph)

print("Word Frequencies:")
for word, count in frequency_result.items():
    print(f"{word}: {count}")
