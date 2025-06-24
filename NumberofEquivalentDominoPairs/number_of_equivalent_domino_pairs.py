from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        count_map = defaultdict(int)
        
        for a, b in dominoes:
            if a > b:
                a, b = b, a
            
            key = a * 10 + b
            count_map[key] += 1
            
        total_pairs = 0
        for count in count_map.values():
            if count >= 2:
                total_pairs += (count * (count - 1)) // 2
                
        return total_pairs