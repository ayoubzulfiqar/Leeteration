class Solution:
    def checkExistence(self, s: str) -> bool:
        n = len(s)
        
        if n < 2:
            return False
        
        s_rev = s[::-1]
        
        for i in range(n - 1):
            substring = s[i:i+2]
            if substring in s_rev:
                return True
                
        return False