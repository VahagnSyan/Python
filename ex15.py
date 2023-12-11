'''
Ex.15:
Write a program to count the frequency of words used in a paragraph
'''

def word_frequency(paragraph):
    words = paragraph.split()
    frequency = {}

    for word in words:
        
        word = word.strip(".,@#$%^&()_+-*/\{}[]~`!?").lower()

        if word:
            frequency[word] = frequency.get(word, 0) + 1

    return frequency

# paragraph = input("Enter your text: ")

# result = word_frequency(paragraph)

# for word, count in result.items():
#     print(f"{word}: {count} times")

# Changed version in this file
paragraph_1 = "This is a simple test. This test should pass."
result_1 = word_frequency(paragraph_1)
assert result_1 == {'this': 2, 'is': 1, 'a': 1, 'simple': 1, 'test': 2, 'should': 1, 'pass': 1}, "It is False 1"

paragraph_2 = "/Another test/, testing testing!"
result_2 = word_frequency(paragraph_2)
assert result_2 == {'another': 1, 'test': 1, 'testing': 2}, "It is False 2"

paragraph_3 = "/*"
result_3 = word_frequency(paragraph_3)
assert result_3 == {}, "It is False 3"

print(f"Testing is ok")
