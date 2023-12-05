# Return dictonary, where keys is words in text and values are their counts
def get_words_count(paragraph):
    special_characters = "~`!@#$%^&*()-_=+[]{};:'|,.<>?/ \\0123456789"
    temp_string = ''
    result = {}

    for i in paragraph:
        if i not in special_characters:
            temp_string += i
        elif temp_string:
            result[temp_string] = result.get(temp_string, 0) + 1
            temp_string = ''

    if temp_string:
        result[temp_string] = result.get(temp_string, 0) + 1

    return result

# Print dictionary items
def print_dictionary(some_dict):
    print("word | frequency\n----------------")
    for key, value in some_dict.items():
        print(key, value, sep=' | ')

some_paragraph = input("Enter your text: ")
print_dictionary(get_words_count(some_paragraph))