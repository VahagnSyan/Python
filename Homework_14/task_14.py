'''
    ex. 14
    Գրել ծրագիր, որը կհաշվի սթրինգի տարրերի կրկնությունների քանակը
    և այն կվերադարձնի dict֊ի միջոցով։
'''


def count_of_elements(str_obj):                                                  
    dict_obj = {}                                                                
    for element in str_obj:                                                      
        dict_obj[element] = dict_obj.get(element, 0)  + 1                                
    
    return dict_obj                                                                   


str_obj = input('Enter the string: ')                                         
print(count_of_elements(str_obj))  

