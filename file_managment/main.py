import random

def generate_random_string():
    chars = ["a", "b", "c"]
    random_string = ''.join(random.choice(chars) for _ in range(3))
    return random_string


with open("random_words.txt", 'w') as file:
    for _ in range(20):
        random_word = generate_random_string()
        file.write(random_word + '\n')

with open("random_words.txt", 'r') as file:
        unique_words = open("unique_words.txt", 'w')
        same_words = open("same_words.txt", 'w')
        same_words_set = set()
        file_words = file.readlines()
        unique_words_set = set()
        for word in file_words:
            if word not in unique_words_set:
                unique_words.write(word)
                unique_words_set.add(word)
            elif word not in same_words_set:
                same_words.write(word)
                same_words_set.add(word)
        unique_words.close()
        same_words.close()