arr_text = "vebfqo ovfeqoj v"

def frequency_count(arr_text):
    count_dict = {}

    for char in arr_text:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict

result = frequency_count(arr_text)
print(result)

"""str_char = "asscewhii  vbiqx"

def str_dict(str_char):
    char_count = {}
    for char in str_char:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

result = str_dict(str_char)
print(result)"""