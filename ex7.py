'''
write functions for the following string operations
* startswith(str_obj, sub_string)
'''

#START
given_str="This is my text"
key="Thi"
def startswith(str_obj, sub_string):
    n=len(str_obj)
    if sub_string[:n]==str_obj:
        return True
    else:
        return False
a=startswith(key, given_str)
if a==True:
    print("String starts with _", eval('key'))
if a == False:
    print("String don't start with _", eval('key'))
