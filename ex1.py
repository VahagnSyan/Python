'''
Given list is  [10, 20, 33, 46, 55]
Divisible by 5
10
20
55

'''
inputList=[10, 20, 33, 46, 55]
print("Divisible by 5")
for i in inputList:
    if i % 5 == 0:
        print(i)
