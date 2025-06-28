import collections

class Solution:
    def maxLengthSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        max_length = 0
        left = 0
        char_counts = collections.Counter()
        bad_char_types = 0 

        for right in range(n):
            char_counts[s[right]] += 1
            if char_counts[s[right]] == 3:
                bad_char_types += 1

            while bad_char_types > 0:
                if char_counts[s[left]] == 3:
                    bad_char_types -= 1
                char_counts[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length