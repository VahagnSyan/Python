'''
    Գրեք ֆունկցիա, որը ստանում է ներդրված  ցուցակներ և 
    վերադարձնում է տրված ցուցակի ներդրված ցուցակների 
    բոլոր էլեմենտները պարունակող մի ցուցակ: 
    Օրինակ
    մուտքագրված է  -> [['a', 'b'], ['c', 'd']]
    Աարդյունքը պետք է լինի ['a', 'b', 'c', 'd: '].

'''

input_list = [["a", "b"], ["c", "d"]]

def mix_nested_lists(lst):
    return [element for sublist in lst for element in sublist]

print(mix_nested_lists(input_list))
