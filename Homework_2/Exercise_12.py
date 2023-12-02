"""
Գրեք ֆունկցիա, որը ստանում է ներդրված  ցուցակներ և 
վերադարձնում է տրված ցուցակի ներդրված ցուցակների 
բոլոր էլեմենտները պարունակող մի ցուցակ: 
Օրինակ մուտքագրված է  -> [['a', 'b'], ['c', 'd']]
Աարդյունքը պետք է լինի ['a', 'b', 'c', 'd: '].
"""


__result_list__ = [] 
def extended_list(input_list):
    if type(input_list) != list:
        __result_list__.append(input_list)
    else:
        for i in input_list:
            extended_list(i)

    return __result_list__

input_list = [['a', 'b'], ['c', 'd'],[[['f', 'g'], ['e', 'h']]]]
result_list = extended_list(input_list)
print(result_list)