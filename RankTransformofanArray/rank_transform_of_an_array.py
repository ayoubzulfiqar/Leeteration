class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        sorted_unique_elements = sorted(list(set(arr)))
        
        value_to_rank_map = {}
        for i, num in enumerate(sorted_unique_elements):
            value_to_rank_map[num] = i + 1
        
        result = []
        for num in arr:
            result.append(value_to_rank_map[num])
            
        return result