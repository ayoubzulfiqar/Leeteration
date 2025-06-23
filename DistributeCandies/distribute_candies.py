class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        n = len(candyType)
        eat_limit = n // 2
        
        unique_types = set(candyType)
        unique_types_count = len(unique_types)
        
        return min(unique_types_count, eat_limit)