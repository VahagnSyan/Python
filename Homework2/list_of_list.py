'''
Գրեք ֆունկցիա, որը ստանում է ներդրված  ցուցակներ և վերադարձնում է 
տրված ցուցակի ներդրված ցուցակների բոլոր էլեմենտները պարունակող մի ցուցակ:
Օրինակ մուտքագրված է  -> [['a', 'b'], ['c', 'd']]
Աարդյունքը պետք է լինի ['a', 'b', 'c', 'd: '].
'''


def flatten_lists(lists):
    flattened_list = []
    for sublist in lists:
        if isinstance(sublist, list):
            flattened_list += flatten_lists(sublist)
        else:
            flattened_list.append(sublist)
    return flattened_list

input_lists = [['a', 'b'], ['c', 'd'], [['v', 'f'], ['k']]]

flattened_result = flatten_lists(input_lists)

print(flattened_result)
