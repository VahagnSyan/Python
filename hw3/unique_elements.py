def clean_input(x):
    return (
        str(x)
        .replace(",", "")
        .replace(" ", "")
        if isinstance(x, str)
        else x
    )


def remove_duplicates(input_list):
    unique_list = []

    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list


user_input = input("Enter the list: ")
input_list = clean_input(user_input)

result_list = remove_duplicates(input_list)
print(result_list)

