'''
write functions for the following string operations
* is_in_str(str_obj, sub_string)
'''

#END
given_str="Hello my World"
key=(input("Enter the letter you want  to  check\n _"))

if key.isdigit(): #check if key is number
    input("Enter the letter you want  to  check\n _")

print("Our text is:")
print(given_str)
print("-//-//-//-")
count = 0
for i in given_str:
    if i==key:
        count=count+1
if count==0:
    print("the letter doesn't find")
else:
    print("the letter finds this much time:") 
    print(count)