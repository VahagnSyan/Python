'''
    Ex.16
    Գրեք ֆունկցիա, որը ստանում է կրկնվող էլեմենտներով լիստ  
    և վերադարձնում է նոր լիստ՝ տրված լիստի չկրկնվող էլեմենտներով։
'''


def unique_elements(input_list):
    element_count = {}
    
    for element in input_list:
        element_count[element] = element_count.get(element, 0) + 1

    result = []
    for element, count in element_count.items():
        if count == 1:
            result.append(element)
            
    return result
    
input_list = ['Hello', 'world', 'Hello', 1, 2, 1, 3, True, False, False]

print(f'Original list: {input_list}')
print(f'Unique elements of list: {unique_elements(input_list)}')
