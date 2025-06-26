class Solution:
    def longestUnequalAdjacentGroupsSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        n = len(words)
        
        dp = [(1, -1)] * n
        
        max_len = 0
        end_idx = -1
        
        for i in range(n):
            for j in range(i):
                if groups[j] != groups[i]:
                    if dp[j][0] + 1 > dp[i][0]:
                        dp[i] = (dp[j][0] + 1, j)
            
            if dp[i][0] > max_len:
                max_len = dp[i][0]
                end_idx = i
        
        result = []
        current_idx = end_idx
        
        while current_idx != -1:
            result.append(words[current_idx])
            current_idx = dp[current_idx][1]
            
        return result[::-1]