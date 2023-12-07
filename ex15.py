'''
Ex.15:
Write a program to count the frequency of words used in a paragraph
'''

def word_frequency(paragraph):
    words = paragraph.split()
    frequency = {}

    for word in words:
        
        word = word.strip(".,!?").lower()

        if word:
            frequency[word] = frequency.get(word, 0) + 1

    return frequency

paragraph = input("Enter your text: ")

result = word_frequency(paragraph)

for word, count in result.items():
    print(f"{word}: {count} times")
