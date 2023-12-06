'''
Գրեք ծրագիր, որը կհաշվի պարագրաֆում օգտագործված բառերի հաճախականությունը
'''

def word_frequency(paragraph):

    split_paragraph = paragraph.split()
    word_frequency = {}

    for word in split_paragraph:

        word = word.strip("~`!@#$%^&*()-_=+[];:'|,.<>?/ \\0123456789").lower()
        if word:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1
        
    return word_frequency

paragraph = input("Enter the text :")
frequency = word_frequency(paragraph)

for word, frequency in frequency.items():
    print(f'Word :{word} - Frecuancy :{frequency}')