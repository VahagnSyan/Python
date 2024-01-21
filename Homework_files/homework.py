'''
Homework using 2 functions to generate random data 
and filter that data into a custom email
'''


import random
from datetime import datetime
import time


def create_csv_file():
    '''
    Create a .csv file, with random people datas
    '''
    names = ['Vahagn', 'Saqo', 'Tyom', 'Alvard', 'Lilia',
             'Gevor', 'Kamo', 'Jean-Claude', 'Billie', 'Jackie']
    surnames = ['Sargsyan', 'Ghalechyan', 'Hovsepyan',
                'Hovakimyan', 'Manukyan', 'Vardanyan',
                'Harutyunyan', 'Van-Damme', 'Eilish', 'Chan']
    ages = [20, 16, 36, 14, 27, 22, 25, 13, 19, 44]
    emails = ['spanchbob@gmail.com',
              'djvaraprust@gmail.com',
              'Jasonstatham@gmail.com',
              'elenioragiry@gmail.com',
              'slovapacana@gmail.com']
    with open('People.csv', 'w', encoding='utf-8') as file:
        random_row = ''
        file.write('name,surname,age,email,time\n')
        for _ in range(20):
            random_row += random.choice(names) + ','
            random_row += random.choice(surnames) + ','
            random_row += str(random.choice(ages)) + ','
            random_row += random.choice(emails) + ','
            random_row += datetime.now().strftime("%H:%M:%S:%f")[:-4] + '\n'
            file.write(random_row)
            time.sleep(0.5)
            random_row = ''



def filter_csv():
    '''
    Filter csv file, and create a new csv file, with latest updated info
    '''
    info_dict = {}

    with open('People.csv', 'r', encoding='utf-8') as file:
        header = file.readline().strip()

        for line in file:
            rows = line.strip().split(',')
            email = rows[3]
            row_time = rows[4]
            if email in info_dict:
                if row_time > info_dict[email][1]:
                    info_dict[email] = (line, row_time)
            else:
                info_dict[email] = (line, row_time)

    with open('Result.csv', 'w', encoding='utf-8') as result:
        result.write(header + '\n')
        for email, (line, row_time) in info_dict.items():
            result.write(line)


create_csv_file()
filter_csv()
