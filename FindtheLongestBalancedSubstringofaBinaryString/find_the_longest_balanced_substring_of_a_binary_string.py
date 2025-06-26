class Solution:
    def longestBalancedSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0

        for k in range(n - 1):
            if s[k] == '0' and s[k+1] == '1':
                count0 = 0
                count1 = 0
                
                left = k
                while left >= 0 and s[left] == '0':
                    count0 += 1
                    left -= 1
                
                right = k + 1
                while right < n and s[right] == '1':
                    count1 += 1
                    right += 1
                
                min_counts = min(count0, count1)
                max_len = max(max_len, 2 * min_counts)
        
        return max_len