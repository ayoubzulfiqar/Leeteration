class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        temp = (s + s)[1:-1]
        return s in temp