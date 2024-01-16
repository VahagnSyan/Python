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
        same_words_set = set()
        file_words = file.readlines()
        unique_words_set = set()
        for word in file_words:
            if word in unique_words_set:
                same_words_set.add(word)
                unique_words_set.remove(word)
            else:
                unique_words_set.add(word)

        with open("unique_words.txt", 'w') as unique_words:
            for word in unique_words_set:
                unique_words.write(word)

        with open("same_words.txt", 'w') as same_words:
            for word in same_words_set:
                same_words.write(word)
