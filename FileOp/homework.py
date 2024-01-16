'''
    Task:
    Write a program to create a file and fill them with random text and
    create file1 where you store the repeated lines and file2 the unique lines
'''

import random

class Task:
    def create_files(self):
        '''
        This function creates a file and fills it with 20 random lines
        '''
        _words = ['Lorem', 'Ipsum', 'is simply', 'dummy text', 'of']
        _chack = [True, False]
        _count = (1, 2, 3)
        _text = []
        with open('file.txt', 'w', encoding='utf-8') as file:
            i = 0
            while i < 20:
                t = ' '.join(random.choice(_words) for _ in range(5))
                if random.choice(_chack):
                    _random_row = random.choice(_count)
                    for _ in range(_random_row):
                        _text.append(t + '\n')
                        i += _random_row - 1
                else:
                    _text.append(t + '\n')
                    i += 1
            _random_text = random.sample(_text, len(_text))
            file.write(''.join(_random_text))
    def create_rep_uniq_files(self):
        '''
        This function creates two files for repeated and unique files
        '''
        with open('file.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            unique_lines = set()
            repeated_lines = set()

            for line in lines:
                if line in unique_lines:
                    repeated_lines.add(line)
                else:
                    unique_lines.add(line)
            with open('Repeat.txt', 'w', encoding='utf-8') as repeat:
                repeat.write(''.join(repeated_lines))
            with open('Unique.txt', 'w', encoding='utf-8') as unique:
                unique.write(''.join(unique_lines))

test = Task()
test.create_files()
test.create_rep_uniq_files()
