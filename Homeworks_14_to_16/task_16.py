'''
Ex.16
Գրեք ֆունկցիա, որը ստանում է կրկնվող էլեմենտներով լիստ  
և վերադարձնում է նոր լիստ՝ տրված լիստի չկրկնվող էլեմենտներով։
'''


def unique_elements(input_list):
    result = []
    for element in input_list:
        if input_list.count(element) == 1:
            result.append(element)
    return result                        
                                                                               
input_list = ['Hello', 'world', 'Hello', 1, 2, 1, 3, True, False, False]                               

print(f'Original list: {input_list}')
print(f'Unique elements of list: {unique_elements(input_list)}')
