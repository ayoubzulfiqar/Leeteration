class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if (k | n) != n:
            return -1
        
        diff_mask = n ^ k
        
        changes = bin(diff_mask).count('1')
        
        return changes