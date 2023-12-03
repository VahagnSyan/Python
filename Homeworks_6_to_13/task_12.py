'''
    Ex. 12
    Գրեք ֆունկցիա, որը ստանում է ներդրված  ցուցակներ և վերադարձնում է տրված
    ցուցակի ներդրված ցուցակների բոլոր էլեմենտները պարունակող մի ցուցակ: Օրինակ
    մուտքագրված է  -> [['a', 'b'], ['c', 'd']]
    Աարդյունքը պետք է լինի ['a', 'b', 'c', 'd: '].
'''
def flatten_list(nested_list):
    result_list = []

    for element in nested_list:
        if type(element) == list:
            result_list.extend(flatten_list(element))
        else:
            result_list.append(element)

    return result_list

original_list = [1, [2, 3], [[4]]]
result = flatten_list(original_list)
print(f'Original list is: {original_list}')
print(f'Flatten list is: {result}')
