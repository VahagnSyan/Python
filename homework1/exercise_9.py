"""
    write functions for the following string operations
    is_in_str(str_obj, sub_string)

"""

def is_in_str(string, substring):
    len_sub = len(substring)
    len_str = len(string)
    i = 0

    while i < len_str-len_sub:
        if string[i : i+len_sub]:
            return True
        else:
            i += 1

    return False

def main():
    text = "ababababab"
    substring = "ab"

    result = is_in_str(text, substring)
    print(f"{result}")

main()
