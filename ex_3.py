'''
Print characters from a string that are present at an even index number
'''


def even_index_characters(input_string):
    even_index_characters = input_string[::2]
    return even_index_characters


string = input("Enter a string: ")
result = even_index_characters(string)
print(f"Characters at even indices: {result}")