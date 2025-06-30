import collections

class Solution:
    def findValidPair(self, s: str) -> str:
        digit_counts = collections.Counter(s)

        for i in range(len(s) - 1):
            digit1_char = s[i]
            digit2_char = s[i+1]

            if digit1_char == digit2_char:
                continue

            val1 = int(digit1_char)
            val2 = int(digit2_char)

            actual_count1 = digit_counts[digit1_char]
            actual_count2 = digit_counts[digit2_char]

            if actual_count1 == val1 and actual_count2 == val2:
                return digit1_char + digit2_char
        
        return ""