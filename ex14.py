
'''
function couns how many times 
does the same letter occur!
'''

text='how many times does the same letter occur!'
dic={}
for i in text:
    if i in dic:
        count=dic[i]
        count=count+1
        dic.update({i: count})
    else:
        dic.update({i: 1})
for key, value in dic.items():
    print(key, value, sep='->')
