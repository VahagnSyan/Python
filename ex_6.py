'''
write a function that returns the number of non-overlapping
occurrences of substring sub in string S
i.e. write a function that does the same as a builtin str.count() function does
function signature: count_sub_in_str(string_obj, substring)
'''


def count_sub_in_str(string_obj, substring):
    count_of_charcters_in_word = 0
    count_of_words_in_string = 0

    for i in range(len(string_obj) - len(substing) + 1):
        for j in range(len(substring)):

            if string_obj[i + j] == substring[j]:
                count_of_charcters_in_word += 1
            else:
                count_of_charcters_in_word = 0
                break

        if len(substring) == count_of_charcters_in_word:
            count_of_words_in_string += 1

        count_of_charcters_in_word = 0

    return count_of_words_in_string


string_obj = input("Enter string object :")
substing = input("Enter substring :")

print("Count of words in string = ", count_sub_in_str(string_obj, substing))
