class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            char_value = ord(char) - ord('A') + 1
            result = result * 26 + char_value
        return result