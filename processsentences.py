"""
Random Sentences Processor

This script generates random sentences, processes them, and saves the results in separate files.
"""

import random

def generate_random_sentence(length=3):
    """
    Generate a random sentence of a given length.

    Parameters:
        length (int): The length of the generated sentence.

    Returns:
        str: The generated random sentence.
    """
    return ''.join(random.choice("abcd") for _ in range(length))

def process_sentences():
    """
    Process sentences:
    1. Generate 35 random sentences and write to 'sent.txt'.
    2. Read sentences from 'sent.txt'.
    3. Identify and collect repeated sentences.
    4. Read existing repeated sentences from 'repeated_sentences.txt'.
    5. Only add new repeated sentences to 'repeated_sentences.txt'.
    6. Write unique sentences to 'unique_sentences.txt'.
    7. Append new repeated sentences to 'repeated_sentences.txt'.
    """
    # Step 1: Generate 35 random sentences and write to 'sent.txt'
    sentences = [generate_random_sentence() for _ in range(35)]
    with open('sent.txt', 'w', encoding='utf-8') as sent_file:
        sent_file.write('\n'.join(sentences))

    # Step 2: Read sentences from 'sent.txt'
    with open('sent.txt', 'r', encoding='utf-8') as sent_file:
        content = sent_file.read().splitlines()

    # Step 3: Identify and collect repeated sentences
    repeated_sentences = [sentence for sentence in content if content.count(sentence) > 1]

    # Step 4: Read existing repeated sentences from 'repeated_sentences.txt'
    existing_repeated_path = 'repeated_sentences.txt'
    existing_repeated = set()
    if os.path.exists(existing_repeated_path):
        with open(existing_repeated_path, 'r', encoding='utf-8') as existing_file:
            existing_repeated = set(existing_file.read().splitlines())

    # Step 5: Only add new repeated sentences to 'repeated_sentences.txt'
    new_repeated_sentences = set(repeated_sentences) - existing_repeated

    # Step 6: Write unique sentences to 'unique_sentences.txt'
    with open('unique_sentences.txt', 'w', encoding='utf-8') as unique_file:
        unique_file.write('\n'.join(list(set(content))))

    # Step 7: Append new repeated sentences to 'repeated_sentences.txt'
    with open(existing_repeated_path, 'a', encoding='utf-8') as repeated_file:
        for new_sentence in new_repeated_sentences:
            if new_sentence not in existing_repeated:
                repeated_file.write(new_sentence + '\n')

process_sentences()
