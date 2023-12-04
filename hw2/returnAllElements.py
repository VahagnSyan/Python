'''

Գրեք ֆունկցիա, որը ստանում է ներդրված  ցուցակներ և վերադարձնում է տրված ցուցակի ներդրված ցուցակների բոլոր էլեմենտները պարունակող մի ցուցակ: Օրինակ
մուտքագրված է  -> [['a', 'b'], ['c', 'd']]
Աարդյունքը պետք է լինի ['a', 'b', 'c', 'd: '].

'''


def merged_list(lists):
    result = []
    for sublist in lists:
        for item in sublist:
            result.append(item)
    return result

user_input = input("Enter values with spaces: ")
input_lists = [user_input.split()]

merged_list_result = merged_list(input_lists)

print(f"Merged List: {merged_list_result}")

