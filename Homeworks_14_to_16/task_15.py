'''
    Ex.15
    Գրեք ծրագիր, որը կհաշվի պարագրաֆում  օգտագործված բառերի հաճախականությունը
'''


def count_of_words(paragraph):                                                    
    marks = "\\!()-[]=+}{;:',<>./?@#$%^&*_~'\"|"

    for symbol in marks:
        paragraph = paragraph.replace(symbol, "")

    paragraph_to_list = paragraph.split()
    result = dict()                                                                
     
    for word in paragraph_to_list:                                                         
        result[word] = result.get(word, 0) + 1                                 
   
    return result                                                              
                                                                               
paragraph_input = input("Enter the paragraph: ")                               
count = count_of_words(paragraph_input)                                     
                                                                               
print(f'The count of words are:\n{count}')
