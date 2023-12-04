""" ex12.py

    Գրեք ֆունկցիա, որը ստանում է ներդրված  ցուցակներ և վերադարձնում է
    տրված ցուցակի ներդրված ցուցակների բոլոր էլեմենտները պարունակող մի ցուցակ:
    Օրինակ
    մուտքագրված է  -> [['a', 'b'], ['c', 'd']]
    Աարդյունքը պետք է լինի ['a', 'b', 'c', 'd: '].
"""

input_list = [['a', 'b'], ['c', 'd']]
extended_list = []

def extend_list(inp_list):
    if type(inp_list) != list:
        extended_list.append(inp_list)
    else:
        for i in inp_list:
            extend_list(i)
    return extended_list

output_list = extend_list([['a', 'b'], ['c', 'd'], [['e', 'f']]])
print(output_list)

