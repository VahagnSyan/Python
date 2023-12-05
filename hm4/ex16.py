"""
    Գրեք ֆունկցիա, որը ստանում է կրկնվող էլեմենտներով լիստ և վերադարձնում է նոր լիստ՝ տրված լիստի չկրկնվող էլեմենտներով։

"""

array = ['Lorem', 'Ipsum', 'is', 'is', 'is']


def uniq(array):
    array = set(array)
    array = list(array)
    print(array)


if __name__ == "__main__":
    uniq(array)




