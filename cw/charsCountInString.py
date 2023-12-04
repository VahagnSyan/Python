def element_count(element, string):
    count = 0
    for i in string:
        if i == element:
            count += 1
    return count

def create_dict(string):
    result = {}
    for i in string:
        if i not in result:
            char_count = element_count(i, string)
            result[i] = char_count
    return result

string = str(input("Input the line: ")) 
result_dict = create_dict(string)
print(result_dict)

