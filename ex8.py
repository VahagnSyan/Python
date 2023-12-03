'''
write functions for the following string operations
* endswith(str_obj, sub_string)
'''

#END
given_str="Hello my World"
key=(input("Enter the letter you want  to  check\n _"))

if key.isdigit(): #check if key is number
    input("Enter the letter you want  to  check\n _")

print("Our text is:")
print(given_str)
                    #compare the als element with key
def endswith(str_obj, sub_string):
    if sub_string[-1]==str_obj:
        print("String ends with key ")
    else:
        print("String dosen't end with key ")
endswith(key, given_str)