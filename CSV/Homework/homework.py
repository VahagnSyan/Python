'''
    This module provides functions to create a CSV file with random data and
    filter rows with the latest time for each unique email.
'''

from datetime import datetime
import random
import time
import sys


def create_file():
    '''
    This function creates a file and fills it with 20 random (csv) lines
    '''
    names = ["Alice", "Bob", "Charlie", "David", "Eva",
             "Frank", "Grace", "Henry", "Ivy", "Jack"]
    surnames = ["Anderson", "Brown", "Clark", "Davis","Evans",
                "Fisher", "Garcia", "Hill", "Ivanov", "Johnson"]
    emails = ["albob@gmail.com", "char_ank@mail.ru", "ivy_hil@gmail.com",
             "fish_vid@mail.ru", "j_clark@gmail.com", "hen_son@gmail.com"]
    age = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27]

    with open('Peoples.csv', 'w', encoding='utf-8') as file:
        row = ''
        file.write('name,surname,age,mail,time\n')
        sys.stdout.write('Creating file...\n0% ')
        sys.stdout.flush()
        for _ in range(20):
            row += random.choice(names) + ','
            row += random.choice(surnames) + ','
            row += str(random.choice(age)) + ','
            row += random.choice(emails) + ','
            row += datetime.now().strftime("%H:%M:%S:%f")[:-4] + '\n'
            time.sleep(0.5)
            sys.stdout.write('-')
            sys.stdout.flush()
        file.write(row)
        sys.stdout.write(' 100%\n')

def filter_and_write_file():
    '''
    Writes rows with the latest time for each unique email to a new CSV file.
    '''
    records = {}

    with open('Peoples.csv', 'r', encoding='utf-8') as file:
        header = file.readline().strip()

        for line in file:
            columns = line.strip().split(',')
            email = columns[3]
            updating_time = columns[4]

            if email in records:
                if updating_time > records[email][1]:
                    records[email] = (line, updating_time)
            else:
                records[email] = (line, updating_time)

    with open('Result.csv', 'w', encoding='utf-8') as result:
        result.write(header + '\n')

        for _, (line, _) in records.items():
            result.write(line)

create_file()
filter_and_write_file()
