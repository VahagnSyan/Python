'''
this function gives a number and print only prime numbers in 
range[0,num]
'''
import math     #library for geting sqrt function

#function checks prime condition
def checkPrime(X):
    temp=1      #indicator prime OR not prime
    sqr_X=math.sqrt(X)+1
    for i in range(2,int(sqr_X)): 
        if(X%i==0):
            temp=0
            break
        else:
            continue
    return temp

num=int(input("Enter the number:\n"))
#for each number of range call checkPrime function
for j in range(1,num):
    result=checkPrime(j)
    if result==1:
        print(j)
