
dict ={}
text = "jgnf kjgjhb gjds"
for i in text:
    
    if dict.get(i) is not None:
        temp = dict.get(i)
        temp = int(temp)
        dict[i] = str(temp +1)
        
    else:
        dict.update({i : 1})  
print ({f"{dict}"})
