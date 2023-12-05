"""
    Ex.15
    Գրեք ծրագիր, որը կհաշվի պարագրաֆում  օգտագործված բառերի 
    հաճախականությունը
"""


def word_count(string):
    words = string.split()
    result = {}
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result


input_text = input("Enter the text: ")
result = word_count(input_text)

print(result)
