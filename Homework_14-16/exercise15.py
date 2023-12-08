'''
    Write a program to count the frequency of words used in a paragraph.

'''

def words_count(paragraph):
    characters = "\\!()-[]}{;:',<>./?@#$%^&*_~'\"|"

    # Replace characters with spaces
    cleaned_paragraph = paragraph
    for symbol in characters:
        cleaned_paragraph = cleaned_paragraph.replace(symbol, " ")

    result = {}
    # Split the paragraph into words
    words = cleaned_paragraph.split()

    for word in words:
        result[word] = result.get(word, 0) + 1
    return result

paragraph_input = input("Enter the paragraph: ")
word_counts = words_count(paragraph_input)

print("Word count in the text:")
for k, v in word_counts.items():
    print(f"The count of '{k}' is {v}.")

