# Return dictonary, where keys is text symbols and values are their counts
def get_symbol_frequency(some_text):
    result = {}
    for i in some_text:
        result[i] = result[i] + 1 if i in result else 1
    
    return result

input_string = input("Enter the some text: ")
result = get_symbol_frequency(input_string)

for key, value in result.items():
    print(key, value, sep=': ')