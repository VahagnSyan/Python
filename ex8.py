'''
write functions for the following string operations
* endswith(str_obj, sub_string)
'''

#END
given_str="Hello my World!"
key=(input("Enter the letter you want  to  check\n _"))

print("Our text is:")
print(given_str)
                    #compare the last elements with key
def endswith(str_obj, sub_string):
    n=len(key)
    m=len(sub_string)
    if sub_string[m-n:]==str_obj:
        print("String ends with", eval('key'))
    else:
        print("String dosen't end with" , eval('key'))
endswith(key, given_str)