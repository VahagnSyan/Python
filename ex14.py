text = input("Enter text: ")
result = {}
for i in text:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
        #print(i,result[i])
print(f"Result is: {result}")
