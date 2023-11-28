print("Text: ")
str_value = str(input())
print("Even index number is: ")
for index, char in enumerate(str_value):
    if index % 2 == 0:
        print(char)
