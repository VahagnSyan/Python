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