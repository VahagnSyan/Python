"""
    write functions for the
    endswith(str_obj, sub_string)

"""

def ends_with(str_obj, sub_string):
    return str_obj[len(str_obj)-len(sub_string) :] == sub_string

def main():
    string = "Hello, world!"
    substring = "ld!"

    if ends_with(string, substring):
        print(f"The string ends with '{substring}'")
    else:
        print(f"The string does not end with '{substring}'")

main()
