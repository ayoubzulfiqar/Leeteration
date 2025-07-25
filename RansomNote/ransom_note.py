import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counts = collections.Counter(magazine)
        
        for char in ransomNote:
            if magazine_counts[char] == 0:
                return False
            magazine_counts[char] -= 1
            
        return True