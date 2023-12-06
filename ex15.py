
'''
function counts how many times 
does the same word occur in sentence.!
'''
import re

text = "Government of the people, by the people, and for the people. shall not perish from the earth."
    #get separated words in list, then iterating in list
arr = re.split("[ ,.]", text)
#print(my_list)
dic = {}
for i in arr:
    if i in dic:
        count = dic[i]
        count = count+1
        dic.update({i: count})
    else:
        dic.update({i: 1})
print(dic)
