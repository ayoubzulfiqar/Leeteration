class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        n = len(strs)
        if n == 0:
            return 0
        m = len(strs[0])
        
        deleted_columns = 0
        
        for j in range(m):
            for i in range(n - 1):
                if strs[i][j] > strs[i+1][j]:
                    deleted_columns += 1
                    break
                    
        return deleted_columns