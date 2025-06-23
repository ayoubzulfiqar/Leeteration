import collections
import math

class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        if not deck:
            return False

        counts = collections.Counter(deck)
        
        frequencies = list(counts.values())
        
        if not frequencies:
            return False

        current_gcd = frequencies[0]
        
        for i in range(1, len(frequencies)):
            current_gcd = math.gcd(current_gcd, frequencies[i])
            if current_gcd == 1:
                return False
        
        return current_gcd > 1