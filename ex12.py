'''
Join all elements of all invested lists in one list!
'''

list1=[1,3,5,7]
list2=[2,4,8,10]
list3=['a','b','c','d']
my_list=[list1, list2, list3]
print("the initial list is:\n", my_list)
#join all elements in one list!
all_list=[]
for i in my_list:
    for j in range(len(i)):
        all_list.append(i[j])

print("\nthe final list is:\n", all_list)