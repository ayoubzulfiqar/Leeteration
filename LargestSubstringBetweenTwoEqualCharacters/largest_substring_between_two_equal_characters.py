class Solution:
    def maxLengthBetweenCharacters(self, s: str) -> int:
        first_occurrence = {}
        max_len = -1

        for i, char in enumerate(s):
            if char in first_occurrence:
                current_len = i - first_occurrence[char] - 1
                max_len = max(max_len, current_len)
            else:
                first_occurrence[char] = i
        
        return max_len