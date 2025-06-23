import collections

class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_counts = collections.Counter(s)
        
        length = 0
        has_odd_count = False
        
        for count in char_counts.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                has_odd_count = True
                
        if has_odd_count:
            length += 1
            
        return length