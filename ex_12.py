'''
Գրեք ֆունկցիա, որը ստանում է ներդրված  ցուցակներ և 
վերադարձնում է տրված ցուցակի ներդրված ցուցակների
բոլոր էլեմենտները պարունակող մի ցուցակ: Օրինակ
մուտքագրված է  -> [['a', 'b'], ['c', 'd']]
Աարդյունքը պետք է լինի ['a', 'b', 'c', 'd: '].
'''


def flatten_nested_lists(nested_lists):
    flattened_list = []
    for sublist in nested_lists:
        for i in sublist:
            if type(i) == list:
                sublist = flatten_nested_lists(sublist) 
        flattened_list.extend(sublist)
    return flattened_list
 

nested_lists = [['a' ,'b'], ['c', 'd'],['e', ['g', ['k', 'l'] ,'h'], 'f']]
result = flatten_nested_lists(nested_lists)
print(result)