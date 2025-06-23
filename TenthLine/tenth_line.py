import sys

try:
    with open('file.txt', 'r') as f:
        line_count = 0
        for line in f:
            line_count += 1
            if line_count == 10:
                sys.stdout.write(line)
                break
except FileNotFoundError:
    pass