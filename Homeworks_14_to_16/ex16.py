""" ex16.py

    Գրեք ֆունկցիա, որը ստանում է կրկնվող էլեմենտներով լիստ և 
    վերադարձնում է նոր լիստ՝ տրված լիստի չկրկնվող էլեմենտներով։
"""

def make_list(input_list):
    output_list = list(set(input_list))
    print(f"\n{input_list = }", f"{output_list = }\n", sep='\n')

make_list([2, 5, 2, 1, 1, 1, 3, 3])

