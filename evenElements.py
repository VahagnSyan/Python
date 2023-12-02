'''
ex.3
Print characters from a string that are present at an even index number
Orginal String is test_text
Printing only even index chars

t
s
_
e
t
'''

string = str(input("Input the string: "))
for i in range(len(string)):
    if i % 2 == 0:
        print(string[i])

