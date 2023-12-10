"""
    Ex.15
    Գրեք ծրագիր, որը կհաշվի պարագրաֆում  օգտագործված բառերի 
    հաճախականությունը
"""


import string

def word_count(string_input):
    for punct in string.punctuation:
        string_input = string_input.replace(punct, ' ')
    words = string_input.split()

    result = {}
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result

input_text = input("Enter the text: ").lower()
result = word_count(input_text)

print(result)
