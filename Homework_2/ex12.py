'''
Գրեք ֆունկցիա, որը ստանում է ներդրված  ցուցակներ և վերադարձնում է տրված ցուցակի ներդրված
ցուցակների բոլոր էլեմենտները պարունակող մի ցուցակ: 
'''

def separated_list(list1):
    list2 = []
    for sublist in list1:
        for item in sublist:
            list2.append(item)
    return list2


list1 = eval(input("Enter the list which contains nasted lists (format [[1, 2], [3, 4]]):"))
print("The seaparated list is :", separated_list(list1))