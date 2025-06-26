class Solution:
    def makeStringsEqual(self, s1: str, s2: str, s3: str) -> int:
        min_len = min(len(s1), len(s2), len(s3))
        
        longest_common_prefix_len = 0
        
        for length in range(min_len, 0, -1):
            prefix1 = s1[0:length]
            prefix2 = s2[0:length]
            prefix3 = s3[0:length]
            
            if prefix1 == prefix2 and prefix2 == prefix3:
                longest_common_prefix_len = length
                break
        
        if longest_common_prefix_len == 0:
            return -1
        else:
            operations = (len(s1) - longest_common_prefix_len) + \
                         (len(s2) - longest_common_prefix_len) + \
                         (len(s3) - longest_common_prefix_len)
            return operations