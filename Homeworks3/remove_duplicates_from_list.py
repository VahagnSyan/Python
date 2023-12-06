"""
    Գրեք ֆունկցիա, որը ստանում է կրկնվող էլեմենտներով լիստ
    և վերադարձնում է նոր լիստ՝ տրված լիստի չկրկնվող էլեմենտներով։
"""


def input_list():
    input_string = input("Enter elements of the list separated by spaces: ")

    list = input_string.split()

    return list


list = input_list()


def remove_duplicates_from_list(list):
    list_duplicate = list.copy()

    i = 0
    while i < len(list_duplicate):
        if list_duplicate[i] in list_duplicate[i + 1 :]:
            list_duplicate.remove(list_duplicate[i])
        else:
            i += 1

    return list_duplicate


print(remove_duplicates_from_list(list))
