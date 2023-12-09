'''
նախադասության մեջ տառերի հաճախականության հաշվելը
'''


def count_of_char_in_str(text):
    dict ={}
    for i in text:
        if dict.get(i) is not None:
            count = dict.get(i)
            count = int(count)
            dict[i] = str(count +1)
        else:
            dict.update({i : 1})  
    return dict


text = input("Enter text :")

print(count_of_char_in_str(text))