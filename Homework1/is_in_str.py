count = 0

def is_in_str(str_obj, sub_string):
    global count
    index = str_obj.find(sub_string)
    if index == -1:
        return False
    else:
        count += 1
        return True

print(is_in_str("vudsbdvbuosdbvu", "buox"))