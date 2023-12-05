# write a function that returns the number of non-overlapping
# occurrences of substring sub in string S
# i.e. write a function that does the same as a builtin str.count() function does
# function signature: count_sub_in_str(string_obj, substring)


def count_sub_in_str(string_obj, substring):
    temp = 0
    count = 0
    for i in range(len(string_obj) - len(substing) + 1):
        for j in range(len(substring)):
            if string_obj[i + j] == substring[j]:
                temp += 1
            else:
                temp = 0
                break
        if len(substring) == temp:
            count += 1
        temp = 0
    return count


string_obj = input("Enter string object :")
substing = input("Enter substring :")

print("count =", count_sub_in_str(string_obj, substing))
