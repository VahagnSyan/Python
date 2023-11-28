"""
write functions for the
startswith(str_obj, sub_string)

"""

def starts_with(str_obj, sub_string):
    return str_obj[:len(sub_string)] == sub_string

def main():
    string = "Hello, world!"
    substring = "Hello"

    if starts_with(string, substring):
        print(f"The string starts with '{substring}'")
    else:
        print(f"The string does not start with '{substring}'")

main()
