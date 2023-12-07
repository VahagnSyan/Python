'''
Գրեք ֆունկցիա, որը ստանում է ներդրված  ցուցակներ և վերադարձնում է տրված ցուցակի ներդրված ցուցակների բոլոր էլեմենտները պարունակող մի ցուցակ: Օրինակ
մուտքագրված է  -> [['a', 'b'], ['c', 'd']]
Աարդյունքը պետք է լինի ['a', 'b', 'c', 'd: '].

'''

def end_lists(nested_lists):
    return [item for sublist in nested_lists for item in sublist]
    
nested_lists = []

while True:
    sublist_str = input("Enter a sublist (press Enter to finish): ")
    if not sublist_str:
        break
    sublist = sublist_str.split()
    nested_lists.append(sublist)
  
print(f"Your nested list is: {nested_lists}")
result = end_lists(nested_lists)
print(f"Result is : {result}")
