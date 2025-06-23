import re

phone_pattern = re.compile(r'^(\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})$')

with open('file.txt', 'r') as f:
    for line in f:
        stripped_line = line.strip()
        if phone_pattern.fullmatch(stripped_line):
            print(stripped_line)