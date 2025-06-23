class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        min_len = float('inf')
        for s in strs:
            min_len = min(min_len, len(s))

        for i in range(min_len):
            char_to_match = strs[0][i]
            
            for j in range(1, len(strs)):
                if strs[j][i] != char_to_match:
                    return strs[0][:i]
        
        return strs[0][:min_len]