"""
Գրեք ֆունկցիա, որը ստանում է ներդրված  ցուցակներ և վերադարձնում է
տրված ցուցակի ներդրված ցուցակների բոլոր էլեմենտները պարունակող մի ցուցակ:
Օրինակ
մուտքագրված է  -> [['a', 'b'], ['c', 'd']]
Արդյունքը պետք է լինի ['a', 'b', 'c', 'd: '].
"""

list = [["a", "b"], ["c", "d"]]


def mix_nested_lists(list):
    merged_list = []

    for sublist in list:
        # Adds every element of subarray to merged_list
        merged_list.extend(sublist)

    return merged_list


print(mix_nested_lists(list))
