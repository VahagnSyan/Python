"""
    write a function that returns the number of non-overlapping occurrences of substring sub in string

"""

def count_sub_in_str(string, substring):
    count = 0
    len_sub = len(substring)
    len_str = len(string)
    i = 0

    while i < len_str-len_sub:
        if string[i : i+len_sub]:
            count += 1
            i += len_sub
        else:
            i += 1

    return count


def main():
    text = "ababababab"
    substring = "ab"

    result = count_sub_in_str(text, substring)
    print(f"Number of non-overlapping occurrences of '{substring}' in '{text}': {result}")

main()