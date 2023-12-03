"""
    Ex. 12
    Գրեք ֆունկցիա, որը ստանում է ներդրված  ցուցակներ և վերադարձնում է տրված 
    ցուցակի ներդրված ցուցակների բոլոր էլեմենտները պարունակող մի ցուցակ: 
"""


def flatten_lists(lists):
    new_list = []
    for sublist in lists:
        for item in sublist:
            new_list.append(item)
    return new_list

input_lists = [['a', 'b'], ['c', 'd']]
result = flatten_lists(input_lists)
print(result)

