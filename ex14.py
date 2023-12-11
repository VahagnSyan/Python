text = input("Enter text: ")
result = {}
for i in text:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
        #print(i,result[i])
# print(f"Result is: {result}")

#Testing version

text_1 = "hello"
result_1 = count_characters(text_1)
assert result_1 == {'h': 1, 'e': 1, 'l': 2, 'o': 1}, "Test 1 failed"

text_2 = "programming"
result_2 = count_characters(text_2)
assert result_2 == {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}, "Test 2 failed"

text_3 = "python"
result_3 = count_characters(text_3)
assert result_3 == {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}, "Test 3 failed"

print("All tests passed!")
