'''
    Ex. 14
    Գրել ծրագիր, որը կհաշվի նախադասության մեջ տառերի հաճախականությունը։
'''

def count_of_letters(sentence):
    marks = "\\!()-[]=+}{;:',<>./?@#$%^&*_~'\"|"

    for symbol in marks:
        sentence = sentence.replace(symbol, "")
  
    sentence_to_list = sentence.split()
    result = dict()
  
    for i in sentence:
        if i != " ":
            result[i] = result.get(i,0) + 1
    return result

str_input = input('Enter the sentence: ')
count = count_of_letters(str_input)

print(f'The count of letters are:\n{count}')
