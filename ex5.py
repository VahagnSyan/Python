'''
check if the given number is 
a palindrome number.
'''

number=int(input("Enter a number:"))
our_num=number #we save our inputing number that will not be changed
reverse_num=0
#reversing the number with taking each unit from the opposite side
#end uniting again
while(number>0):
    temp=number%10
    reverse_num=reverse_num*10+temp
    number=number//10
if(our_num==reverse_num):
    print("number is palindrom")
else:
    print("number isn't palindrom")


