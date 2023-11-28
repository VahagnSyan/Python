count = 0

def count_sub_in_str(string_obj, substring):
    global count
    index = string_obj.find(substring)
    if index == -1:
        return count
    else:
        count += 1
        return count_sub_in_str(string_obj[index + len(substring) :], substring)


print(count_sub_in_str("vudsbdvbuosdbvu", "vu"))