class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if sorted([s1[0], s1[2]]) != sorted([s2[0], s2[2]]):
            return False
        if sorted([s1[1], s1[3]]) != sorted([s2[1], s2[3]]):
            return False
        return True