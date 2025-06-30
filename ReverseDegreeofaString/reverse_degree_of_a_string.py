def reverse_degree(s: str) -> int:
    total_degree = 0
    for i, char in enumerate(s):
        reversed_alphabet_pos = 26 - (ord(char) - ord('a'))
        string_pos = i + 1
        total_degree += reversed_alphabet_pos * string_pos
    return total_degree