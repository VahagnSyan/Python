"""
This script generates mixed random student data, writes it to a CSV file,
finds the student with the latest registration time among repeated elements,
and writes that student's data to another file.
"""

import random
import string
from collections import defaultdict
from datetime import datetime, timedelta

def join(separator, *args):
    """
    Join elements using the specified separator without using the join method.

    Parameters:
    - separator (str): The string to use as a separator.
    - *args: Variable number of arguments to join.

    Returns:
    - str: The joined string.
    """
    joined_string = ""
    for i, arg in enumerate(args):
        joined_string += str(arg)
        if i < len(args) - 1:
            joined_string += separator
    return joined_string

def generate_random_student():
    """
    Generate random student data.

    Returns:
    - dict: Random student data with 'name', 'surname', 'age', and 'registration_time'.
    """
    name = ''.join(random.choices(string.ascii_uppercase, k=random.randint(3, 8)))
    surname = ''.join(random.choices(string.ascii_uppercase, k=random.randint(5, 10)))
    age = random.randint(18, 25)
    current_time = datetime.now()
    registration_time = current_time - timedelta(days=random.randint(1, 365))
    return {'name': name, 'surname': surname, 'age': age, 'registration_time': registration_time}

def generate_student_data_with_repetitions(num_unique_students, num_repetitions):
    """
    Generate a mix of unique and repeated random student data.

    Parameters:
    - num_unique_students (int): Number of unique students to generate.
    - num_repetitions (int): Number of times each student should be repeated.

    Returns:
    - list: List of random student data with a mix of unique and repeated elements.
    """
    unique_students = [generate_random_student() for _ in range(num_unique_students)]
    repeated_students = []
    for student in unique_students:
        repeated_students.extend([student.copy() for _ in range(num_repetitions)])
    return unique_students + repeated_students

def write_csv(file_path, data):
    """
    Write student data to a CSV file.

    Parameters:
    - file_path (str): Path to the output file.
    - data (list): List of dictionaries representing student data.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        header = ','.join(data[0].keys())
        file.write(header + '\n')
        for record in data:
            if isinstance(record['registration_time'], datetime):
                record['registration_time'] = record['registration_time'].strftime("%Y-%m-%d %H:%M:%S")
            file.write(','.join(map(str, record.values())) + '\n')

def find_latest_registration(data):
    """
    Find the student with the latest registration time among repeated elements.

    Parameters:
    - data (list): List of student data.

    Returns:
    - dict: Student data with the latest registration time.
    """
    registration_times = defaultdict(list)
    for student in data:
        unique_identifier = (student['name'], student['surname'])
        registration_times[unique_identifier].append(student)
    latest_students = []
    for group in registration_times.values():
        latest_student = max(group, key=lambda x: x['registration_time'])
        latest_students.append(latest_student)
    overall_latest_student = max(latest_students, key=lambda x: x['registration_time'])
    return overall_latest_student

def write_latest_registration(file_path, data):
    """
    Write the student with the latest registration time among repeated elements to a file.

    Parameters:
    - file_path (str): Path to the output file.
    - data (list): List of student data.
    """
    latest_student = find_latest_registration(data)
    with open(file_path, 'w', encoding='utf-8') as file:
        header = ','.join(latest_student.keys())
        file.write(header + '\n')
        file.write(','.join(map(str, latest_student.values())) + '\n')

# Generate student data and write to files
mixed_students = generate_student_data_with_repetitions(5, 3)
write_csv('mixed_students.csv', mixed_students)

latest_student_file_path = 'latest_student.csv'
write_latest_registration(latest_student_file_path, mixed_students)

# Assert statements to test the output

# Test 1: Check if the generated CSV file contains data
with open('mixed_students.csv', 'r', encoding='utf-8') as file:
    csv_content = file.read()
assert len(csv_content) > 0, "Generated CSV file is empty"

# Test 2: Check if the latest registration file contains data
with open(latest_student_file_path, 'r', encoding='utf-8') as file:
    latest_student_content = file.read()
assert len(latest_student_content) > 0, "Latest registration file is empty"

# Test 3: Check if the latest registration file contains correct data
latest_student_data = find_latest_registration(mixed_students)
with open(latest_student_file_path, 'r', encoding='utf-8') as file:
    header_line = file.readline().strip()
    assert header_line == ','.join(latest_student_data.keys()), "Header mismatch"
    data_line = file.readline().strip()
    assert data_line == ','.join(map(str, latest_student_data.values())), "Data mismatch"

print("All tests passed successfully!")
