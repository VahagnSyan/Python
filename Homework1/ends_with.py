
def endswith(str_obj, sub_string):
    return str_obj[len(str_obj) - len(sub_string) :] == sub_string 


print(endswith("vudsbdvbuosdbvu", "vu"))