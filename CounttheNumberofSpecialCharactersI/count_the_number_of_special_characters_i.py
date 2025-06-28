class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        char_set = set(word)
        special_count = 0
        for i in range(26):
            lowercase_char = chr(ord('a') + i)
            uppercase_char = chr(ord('A') + i)
            if lowercase_char in char_set and uppercase_char in char_set:
                special_count += 1
        return special_count