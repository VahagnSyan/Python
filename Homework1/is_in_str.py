
def is_in_str(str_obj, sub_string):
    index = str_obj.find(sub_string)
    if index == -1:
        return False
    else:
        return True

print(is_in_str("vudsbdvbuosdbvu", "buox"))