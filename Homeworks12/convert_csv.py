from random import randint


def generate_users_file():
    users_template = {
        "names": ["John", "Jane", "Alice", "Bob", "Alice"],
        "surnames": ["Doe", "Smith", "Jones", "Johnson"],
        "phone_numbers": [1234567890, 9876543210, 5551234567, 1112223333, 5551234567],
        "emails": [
            "johndoe@gmail.com",
            "janesmith@gmail.com",
            "alicejones@gmail.com",
            "bobjohnson@gmail.com",
            "alicejones@gmail.com",
        ],
    }

    with open("users.csv", "w", newline="\n") as users_file:
        for i in range(10):
            new_user = []
            for key, value in users_template.items():
                new_user.append(str((value[randint(0, len(users_template)) - 1])))
            users_file.write(" ".join(new_user) + "\n")


def convert_csv(txt_file_path, csv_file_path):
    """
    Read users from a users.csv file, (keeping last occurrence if duplicate email occurs),
    and creates a CSV file.

    @args:
        users_file_path (str): The path to the input users file.
        csv_file_path (str): The path to the output CSV file.
    """

    seen_emails = {}
    unique_users = []

    with open(txt_file_path, "r") as txt_file:
        for line in txt_file:
            name, surname, phone_number, email = line.strip().split()

            seen_emails[email] = (name, surname, phone_number, email)
            if email in seen_emails:
                print(f"Duplicate email '{email}' found. Keeping the last occurrence.")

    unique_users = [list(user_info) for email, user_info in seen_emails.items()]

    with open(csv_file_path, "w", newline="") as csv_file:
        for user_info in unique_users:
            csv_file.write(",".join(user_info) + "\n")


generate_users_file()

users_file_path = "users.csv"
csv_file_path = "unique_users.csv"
convert_csv(users_file_path, csv_file_path)
