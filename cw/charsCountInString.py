def count_elements(string):
    result = {}
    for i in string:
        result[i] = result.get(i, 0) + 1
    return result

string = str(input("Input the line: ")) 
result_dict = count_elements(string)
print(result_dict)

