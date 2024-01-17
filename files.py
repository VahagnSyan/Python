import random

characters = "abcde"
line_count = 20  # Change this to the desired number of lines
repeat_probability = 0.4  # Adjust this to control the probability of lines being repeated

lines = []

for _ in range(line_count):
    line = ''.join(random.choice(characters) for _ in range(5))
    if random.random() < repeat_probability and lines:
        lines.append(random.choice(lines))
    else:
        lines.append(line)

with open('main.txt', 'w', encoding='utf-8') as main_file:
    for line in lines:
        main_file.write(line + '\n')

with open('main.txt', 'r', encoding='utf-8') as main_file:
    lines = main_file.read().splitlines()

line_counts = {}

for line in lines:
    line_counts[line] = line_counts.get(line, 0) + 1

unique_lines = set()
repeated_lines = set()

for line, count in line_counts.items():
    if count == 1:
        unique_lines.add(line)
    else:
        repeated_lines.add(line)

with open('unic_lines.txt', 'w', encoding='utf-8') as unic_file:
    for line in unique_lines:
        unic_file.write(line + '\n')

with open('repeated_lines.txt', 'w', encoding='utf-8') as repeated_file:
    for line in repeated_lines:
        repeated_file.write(line + '\n')

