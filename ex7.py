'''
write functions for the following string operations
* startswith(str_obj, sub_string)
'''

#START
given_str="This is my text"
key="T"
def startswith(str_obj, sub_string):
    if sub_string[0]==str_obj:
        return True
    else:
        return False
a=startswith(key, given_str)
if a==True:
    print("String starts with 'T'")
if a == False:
    print("String don't start with 'T'")
