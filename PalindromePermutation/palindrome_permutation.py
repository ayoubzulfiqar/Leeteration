import collections

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        processed_s = s.replace(" ", "").lower()
        char_counts = collections.Counter(processed_s)
        odd_count = 0
        for count in char_counts.values():
            if count % 2 != 0:
                odd_count += 1
        return odd_count <= 1