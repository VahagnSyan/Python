'''
    Write a program to count the frequency of words used in a paragraph.

'''

def words_count(paragraph):
    result = {}
    words = paragraph.split()
    for word in words:
        result[word] = result.get(word, 0) + 1
    return result

paragraph_input = input("Enter the paragraph: ")
word_counts = words_count(paragraph_input)

print("\nWord count in the text:")
for k, v in word_counts.items():
    print(f"The count of '{k}' is {v}.")

