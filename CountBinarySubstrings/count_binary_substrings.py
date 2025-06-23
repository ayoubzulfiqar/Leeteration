class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        prev_len = 0
        current_len = 1 

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                current_len += 1
            else:
                count += min(prev_len, current_len)
                prev_len = current_len
                current_len = 1
        
        count += min(prev_len, current_len)
        
        return count