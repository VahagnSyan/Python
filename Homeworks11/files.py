import random


def create_files():
    """
    Creates original, duplicates and unique files based on original text file.
    """

    # Create the original file with duplicates
    with open("original_file.txt", "w") as f:
        lines = []
        for i in range(random.randint(5, 10)):
            line = f"Line {random.randint(1, 100)} with some text {random.randint(100, 200)}\n"
            lines.append(line)
            if random.random() < 0.4:
                lines.append(line)
        f.writelines(lines)

    # Create the file with duplicates
    with open("duplicates.txt", "w") as f:
        seen = set()
        for line in open("original_file.txt"):
            if line in seen:
                f.write(line)
            else:
                seen.add(line)

    # Create the file with unique texts
    with open("unique_texts.txt", "w") as f:
        seen = set()
        for line in open("original_file.txt"):
            if line not in seen:
                f.write(line)
                seen.add(line)


create_files()
