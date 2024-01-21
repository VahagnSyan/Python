import random
from datetime import datetime
import time

names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma']
surnames = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown']
ages = [18, 19, 20, 21, 22]
emails = ['alice@email.com', 'bob@email.com', 'charlie@email.com', 'david@email.com', 'emma@email.com']
phones = ['111', '222', '333', '444', '555']

random_students = []
for _ in range(10):
    student = {
        'name': random.choice(names),
        'surname': random.choice(surnames),
        'age': str(random.choice(ages)),
        'email': random.choice(emails),
        'phone': random.choice(phones),
        'createdAt': datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    }
    random_students.append(student)
    time.sleep(1)


with open("students_info.csv", 'w') as file:
    header = ",".join(random_students[0].keys())
    file.write(header + "\n")
    for student in random_students:
        values = [str(student[key]) for key in student]
        file.write(",".join(values) + "\n")


unique_emails = set()
email_info_dict = {}
for student in random_students:
    if student['email'] in unique_emails:
        if student['createdAt'] > email_info_dict[student['email']]['createdAt']:
            unique_emails.remove(student['email'])
            email_info_dict[student['email']] = student
    else:
        unique_emails.add(student['email'])
        email_info_dict[student['email']] = student


with open("students_unique_info.csv", 'a') as file:
    for student in email_info_dict.values():
        values = [str(student[key]) for key in student]
        file.write(",".join(values) + "\n")