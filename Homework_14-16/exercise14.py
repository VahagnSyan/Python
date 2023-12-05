'''
    Count the frequency of letters in a sentence․

'''

def letters_count(sentence):
    result = {}
    for i in sentence:
        result[i] = result.get(i, 0) + 1
    
    return result

sentence_input = input("Enter the text: ")
result = letters_count(sentence_input)

for k, v in result.items():
    print(f"The count of '{k}' is {v}.")

