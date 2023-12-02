'''
write a function that returns the number of non-overlapping
occurrences of substring sub in string S
'''
given_string="python"
n=len(given_string)
my_list=[]
for i in range(0,n):
    for j in range(i,n):
        my_list.append(given_string[i:(j+1)])
print("all subsets of string are:")
count=0
for i in my_list:
    print(i)
    count+=1
print(" ")
print("the count of all subsets:")
print(count)
