"""
    Ex.14  
    նախադասության մեջ տառերի հաճախականության հաշվելը
"""


def char_count(string):
    resault = {}
    for i in string:
        if i in resault:
            resault[i] += 1
        else:
            resault[i] = 1
    return resault


string = input("Enter the text ")
resault = char_count(string)

print(resault) 
