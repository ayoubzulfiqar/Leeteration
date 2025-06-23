class Solution:
    def canWin(self, s: str) -> bool:
        for i in range(len(s) - 1):
            if s[i] == '+' and s[i+1] == '+':
                next_s = s[:i] + "--" + s[i+2:]
                if not self.canWin(next_s):
                    return True
        return False