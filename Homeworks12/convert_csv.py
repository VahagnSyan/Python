def convert_csv(txt_file_path, csv_file_path):
    """
    Read users from a txt file, (keeping last occurrence if duplicate email occurs),
    and creates a CSV file.

    @args:
        txt_file_path (str): The path to the input TXT file.
        csv_file_path (str): The path to the output CSV file.
    """

    seen_emails = {}
    unique_users = []

    with open(txt_file_path, "r") as txt_file:
        for line in txt_file:
            name, surname, phone_number, email, creation_date = line.strip().split()

            if email not in seen_emails:
                seen_emails[email] = (name, surname, phone_number, email, creation_date)
            else:
                print(f"Duplicate email '{email}' found. Keeping the last occurrence.")
                seen_emails[email] = (name, surname, phone_number, email, creation_date)

    unique_users = [list(user_info) for email, user_info in seen_emails.items()]

    with open(csv_file_path, "w", newline="") as csv_file:
        for user_info in unique_users:
            csv_file.write(",".join(user_info) + "\n")


txt_file_path = "users.txt"
csv_file_path = "unique_users.csv"
convert_csv(txt_file_path, csv_file_path)
