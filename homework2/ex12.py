"""
    Գրեք ֆունկցիա, որը ստանում է ներդրված  ցուցակներ և վերադարձնում է տրված ցուցակի ներդրված ցուցակների բոլոր էլեմենտները պարունակող մի ցուցակ: Օրինակ
    մուտքագրված է  -> [['a', 'b'], ['c', 'd']]
    Աարդյունքը պետք է լինի ['a', 'b', 'c', 'd: '].

"""

def extend_list(lists):
    list = []
    for sublist in lists:
        if isinstance(sublist, list):
            list.extend(extend_list(sublist))
        else:
            list.append(sublist)
    return list

def main():
    input_lists_2 = [[1, [2, [3, 4], 5], 6], [7, 8, [9, 10]]]
    result_2 = extend_list(input_lists_2)
    print(result_2)


main()
