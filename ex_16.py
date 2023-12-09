"""
Գրեք ֆունկցիա, որը ստանում է կրկնվող էլեմենտներով լիստ և
վերադարձնում է նոր լիստ՝ տրված լիստի չկրկնվող էլեմենտներով։
"""
def non_repeting_list(lists):
    new_list  = []
    for i in range(len(lists)):
        if new_list == []:
            new_list.append(lists[i])
        for j in range(len(new_list)):
            is_in_list = True
            if lists[i] == new_list[j]:
                is_in_list = False
                break
        if is_in_list:
            new_list.append(lists[i])
    return new_list        


elements = input("Enter numbers separated by space: ")

input_list = elements.split()

print("Non-repeting list : ", non_repeting_list(input_list))

