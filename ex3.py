'''
Orginal String is  test_text
Printing only even index chars

'''
text = str(input("Enter text: "))
new_text = text.split()[0::2]
text = " ".join(new_text)
print(text)
