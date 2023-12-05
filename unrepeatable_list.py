"""
    Ex.16
    Գրեք ֆունկցիա, որը ստանում է կրկնվող էլեմենտներով լիստ և վերադարձնում 
    է նոր լիստ՝ տրված լիստի չկրկնվող էլեմենտներով։
"""


def remove_duplicates(input_list):
    unrepeatable_list = []
    for item in input_list:
        if input_list.count(item) == 1:  # եթե հանդիպում է 1 անգամ
            unrepeatable_list.append(item) # ավելացնում ենք նոր list֊ի մեջ 
    return unrepeatable_list


input_list = input("Enter the list elements separated by space ").split()

result = remove_duplicates(input_list)
print(result)
